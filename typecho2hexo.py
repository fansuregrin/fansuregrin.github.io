import os
from datetime import datetime

import yaml
import pymysql
import dotenv
import mdformat
from pymysql.cursors import Cursor
from tqdm import tqdm


dotenv.load_dotenv()


class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


def get_tags(cursor: Cursor):
    cursor.execute(f"SELECT mid,name FROM {db_prefix}metas WHERE type = 'tag'")
    results = cursor.fetchall()
    tags = dict()
    for row in results:
        mid, name = row
        tags[mid] = name
    return tags


def get_category_tree(cursor: Cursor):
    cursor.execute(f"SELECT mid,name,parent FROM {db_prefix}metas WHERE type = 'category'")
    results = cursor.fetchall()
    categories = dict()
    for row in results:
        mid, name, parent = row
        category = {
            "mid": mid,
            "name": name,
            "parent": parent,
            "children": []
        }
        categories[mid] = category
    category_tree = []
    for mid in categories:
        item = categories[mid]
        parent_id = item["parent"]
        if parent_id == 0:
            category_tree.append(item)
        else:
            categories[parent_id]["children"].append(item)

    return category_tree


def find_category(tree, target_mid, path=None):
    if path is None:
        path = []

    for node in tree:
        current_path = path + [node["name"]]
        if node["mid"] == target_mid:
            return current_path
        if node["children"]:
            result = find_category(node["children"], target_mid, current_path)
            if result:
                return result
    return None


source_dir = "source"
db = pymysql.connect(
    host=os.getenv("TYPECHO_DB_HOST"),
    user=os.getenv("TYPECHO_DB_USER"),
    password=os.getenv("TYPECHO_DB_PASSWORD"),
    database=os.getenv("TYPECHO_DB_DATABASE"),
    port=int(os.getenv("TYPECHO_DB_PORT"))
)
cursor = db.cursor()
db_prefix = os.getenv("TYPECHO_DB_PREFIX")

tags = get_tags(cursor)
category_tree = get_category_tree(cursor)

sql = f"""SELECT c.cid,c.title,c.slug,c.created,c.text,c.type AS c_type,
m.mid,m.name AS m_name,m.type AS m_type
FROM {db_prefix}contents c
LEFT JOIN {db_prefix}relationships r ON c.cid = r.cid
LEFT JOIN {db_prefix}metas m ON r.mid = m.mid
ORDER BY created;
"""
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    contents = dict()
    for row in tqdm(results):
        cid, title, slug, created, text, c_type, mid, m_name, m_type = row
        if cid not in contents:
            created = datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M:%S")
            text: str
            text = text.lstrip("<!--markdown-->")
            text = mdformat.text(text)
            c = {
                "cid": cid,
                "title": title,
                "slug": slug,
                "created": created,
                "text": text,
                "c_type": c_type,
                "tags": [],
                "categories": []
            }
            contents[cid] = c
        else:
            c = contents[cid]

        if m_type == "tag":
            c["tags"].append(m_name)
        elif m_type == "category":
            category = find_category(category_tree, mid)
            c["categories"].append(category)

    for cid in contents:
        c = contents[cid]
        c_type = c["c_type"]
        if c_type == "post":
            out_dir = os.path.join(source_dir, "_posts")
        elif c_type == "page":
            out_dir = os.path.join(source_dir, "_pages")
        else:
            raise NotImplementedError(c_type)
        os.makedirs(out_dir, exist_ok=True)
        meta_info = {
            "title": c["title"],
            "date": c["created"],
        }
        if len(c["categories"]) > 0:
            meta_info["categories"] = c["categories"]
        if len(c["tags"]) > 0:
            meta_info["tags"] = c["tags"]
        meta_info_str = yaml.dump(meta_info, Dumper=IndentDumper,
                                  allow_unicode=True, sort_keys=False).strip()
        with open(os.path.join(out_dir, c["slug"] + ".md"), "w", encoding="utf8") as f:
            f.write(f"---\n{meta_info_str}\n---\n" + c["text"] + "\n")
except Exception as e:
    print(e)
cursor.close()
db.close()
