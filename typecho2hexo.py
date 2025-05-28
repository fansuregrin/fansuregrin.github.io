import os
from datetime import datetime

import pymysql
import dotenv
import mdformat
from tqdm import tqdm


dotenv.load_dotenv()

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
sql = f"SELECT title,slug,created,text,type FROM {db_prefix}contents \
ORDER BY created;"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in tqdm(results):
        title, slug, created, text, type_ = row
        created = datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M:%S")
        text: str
        text = text.lstrip("<!--markdown-->")
        text = mdformat.text(text)
        if type_ == "post":
            out_dir = os.path.join(source_dir, "_posts")
        elif type_ == "page":
            out_dir = os.path.join(source_dir, "_pages")
        else:
            raise NotImplementedError(type_)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, slug + ".md"), "w",
                  encoding="utf8") as f:
            f.write(f"---\ntitle: {title}\ndate: {created}\n---\n"
                    + text + "\n")
except Exception as e:
    print(e)
cursor.close()
db.close()
