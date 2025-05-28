---
title: MySQL中的字符集和校对规则
date: 2024-04-07 14:52:00
---
## 什么是字符集和校对规则

总的来说，字符集 (Character Set) 是一组字符的集合，而校对规则 (Collation) 是比较和排序特定字符集的规则。一个字符集可能关联多个校对规则，而每个校对规则仅关联一个字符集。在 MariaDB 中，字符集名称始终是校对规则名称的一部分。例如，`latin1_german1_ci` 校对规则仅适用于 `latin1` 字符集。每个字符集也有一种默认校对规则。`latin1` 默认校对规则为 `latin1_swedish_ci`。

## 查看字符集和校对规则

在官方版的 MariaDB 中，默认的字符集是 `latin1`，默认的排序规则是 `latin1_swedish_ci`。而 Debian 发行版提供的 MariaDB 的默认字符集是 `utf8mb4`，默认的排序规则是 `utf8mb4_general_ci`，Debian 这样设置的目的是让数据库默认支持 *emoji*。

使用 `SHOW CHARACTER SET`/`SHOW CHARSET` 命令可以查看 MariaDB/MysQL Server 支持的所有字符集：

```SQL
MariaDB [test]> SHOW CHARACTER SET;
+----------+-----------------------------+---------------------+--------+
| Charset  | Description                 | Default collation   | Maxlen |
+----------+-----------------------------+---------------------+--------+
| big5     | Big5 Traditional Chinese    | big5_chinese_ci     |      2 |
| dec8     | DEC West European           | dec8_swedish_ci     |      1 |
| cp850    | DOS West European           | cp850_general_ci    |      1 |
| hp8      | HP West European            | hp8_english_ci      |      1 |
| koi8r    | KOI8-R Relcom Russian       | koi8r_general_ci    |      1 |
| latin1   | cp1252 West European        | latin1_swedish_ci   |      1 |
| latin2   | ISO 8859-2 Central European | latin2_general_ci   |      1 |
| swe7     | 7bit Swedish                | swe7_swedish_ci     |      1 |
| ascii    | US ASCII                    | ascii_general_ci    |      1 |
| ujis     | EUC-JP Japanese             | ujis_japanese_ci    |      3 |
| sjis     | Shift-JIS Japanese          | sjis_japanese_ci    |      2 |
| hebrew   | ISO 8859-8 Hebrew           | hebrew_general_ci   |      1 |
| tis620   | TIS620 Thai                 | tis620_thai_ci      |      1 |
| euckr    | EUC-KR Korean               | euckr_korean_ci     |      2 |
| koi8u    | KOI8-U Ukrainian            | koi8u_general_ci    |      1 |
| gb2312   | GB2312 Simplified Chinese   | gb2312_chinese_ci   |      2 |
| greek    | ISO 8859-7 Greek            | greek_general_ci    |      1 |
| cp1250   | Windows Central European    | cp1250_general_ci   |      1 |
| gbk      | GBK Simplified Chinese      | gbk_chinese_ci      |      2 |
| latin5   | ISO 8859-9 Turkish          | latin5_turkish_ci   |      1 |
| armscii8 | ARMSCII-8 Armenian          | armscii8_general_ci |      1 |
| utf8mb3  | UTF-8 Unicode               | utf8mb3_general_ci  |      3 |
| ucs2     | UCS-2 Unicode               | ucs2_general_ci     |      2 |
| cp866    | DOS Russian                 | cp866_general_ci    |      1 |
| keybcs2  | DOS Kamenicky Czech-Slovak  | keybcs2_general_ci  |      1 |
| macce    | Mac Central European        | macce_general_ci    |      1 |
| macroman | Mac West European           | macroman_general_ci |      1 |
| cp852    | DOS Central European        | cp852_general_ci    |      1 |
| latin7   | ISO 8859-13 Baltic          | latin7_general_ci   |      1 |
| utf8mb4  | UTF-8 Unicode               | utf8mb4_general_ci  |      4 |
| cp1251   | Windows Cyrillic            | cp1251_general_ci   |      1 |
| utf16    | UTF-16 Unicode              | utf16_general_ci    |      4 |
| utf16le  | UTF-16LE Unicode            | utf16le_general_ci  |      4 |
| cp1256   | Windows Arabic              | cp1256_general_ci   |      1 |
| cp1257   | Windows Baltic              | cp1257_general_ci   |      1 |
| utf32    | UTF-32 Unicode              | utf32_general_ci    |      4 |
| binary   | Binary pseudo charset       | binary              |      1 |
| geostd8  | GEOSTD8 Georgian            | geostd8_general_ci  |      1 |
| cp932    | SJIS for Windows Japanese   | cp932_japanese_ci   |      2 |
| eucjpms  | UJIS for Windows Japanese   | eucjpms_japanese_ci |      3 |
+----------+-----------------------------+---------------------+--------+
40 rows in set (0.002 sec)
```

使用 `SHOW COLLATION` 可以查看数据库支持的所有校对规则。

```SQL
MariaDB [test]> SHOW COLLATION LIKE 'latin1%';
+-------------------------+---------+------+---------+----------+---------+
| Collation               | Charset | Id   | Default | Compiled | Sortlen |
+-------------------------+---------+------+---------+----------+---------+
| latin1_german1_ci       | latin1  |    5 |         | Yes      |       1 |
| latin1_swedish_ci       | latin1  |    8 | Yes     | Yes      |       1 |
| latin1_danish_ci        | latin1  |   15 |         | Yes      |       1 |
| latin1_german2_ci       | latin1  |   31 |         | Yes      |       2 |
| latin1_bin              | latin1  |   47 |         | Yes      |       1 |
| latin1_general_ci       | latin1  |   48 |         | Yes      |       1 |
| latin1_general_cs       | latin1  |   49 |         | Yes      |       1 |
| latin1_spanish_ci       | latin1  |   94 |         | Yes      |       1 |
| latin1_swedish_nopad_ci | latin1  | 1032 |         | Yes      |       1 |
| latin1_nopad_bin        | latin1  | 1071 |         | Yes      |       1 |
+-------------------------+---------+------+---------+----------+---------+
10 rows in set (0.000 sec)
```

校对规则的名称中包含了字符集名称，字符集的名称一般作为前缀出现在校对规则的名称里，校对规则的名称的后缀一般有 **ci**、**cs** 和 **bin**，分别代表着大小写不敏感 (Case Insensitive)、大小写敏感 (Case Sensitive) 和 二进制比较 (Binary)。

查看数据库当前的字符集：

```SQL
MariaDB [test]> SHOW VARIABLES LIKE '%character_set%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb3                    |
| character_set_connection | utf8mb3                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb3                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8mb3                    |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.001 sec)
```

查看数据库当前的校对规则：

```SQL
MariaDB [test]> SHOW VARIABLES LIKE '%collation%';
+----------------------+--------------------+
| Variable_name        | Value              |
+----------------------+--------------------+
| collation_connection | utf8mb3_general_ci |
| collation_database   | utf8mb4_general_ci |
| collation_server     | utf8mb4_general_ci |
+----------------------+--------------------+
3 rows in set (0.001 sec)
```

可以使用 `SHOW TABLE STATUS FROM 'db_name' WHERE name='table_name'` 查看表的校对规则。
可以使用 `SHOW FULL COLUMNS FROM 'table_name'` 查看列的校对规则，例如：

```SQL
MariaDB [webserver]> SHOW FULL COLUMNS FROM test;
+----------+----------+--------------------+------+-----+---------+----------------+---------------------------------+---------+
| Field    | Type     | Collation          | Null | Key | Default | Extra          | Privileges                      | Comment |
+----------+----------+--------------------+------+-----+---------+----------------+---------------------------------+---------+
| id       | int(11)  | NULL               | NO   | PRI | NULL    | auto_increment | select,insert,update,references |         |
| username | char(50) | utf8mb4_general_ci | NO   | UNI | NULL    |                | select,insert,update,references |         |
| password | char(50) | utf8mb4_general_ci | NO   |     | NULL    |                | select,insert,update,references |         |
+----------+----------+--------------------+------+-----+---------+----------------+---------------------------------+---------+
3 rows in set (0.001 sec)
```

## 设置字符集和校对规则

字符集和校对规则都可以从*服务器级别* (Server Level) 指定到*列级别* (Column Level)，也可以指定用于客户端-服务器连接。更改字符集而不指定排序规则时，将始终使用新字符集的默认排序规则。

### 在 Server 层级设置字符集和校对规则

`character_set_server` 系统变量可以用来更改默认服务器字符集，它可以在启动时或动态使用中通过`SET`命令设置。类似地，`collation_server` 变量用于设置默认服务器校对规则。例如，下面这个例子将服务器的默认字符集设为了 `latin2`，将默认校对规则设为了 `latin2_czech_cs`。

```SQL
SET character_set_server = 'latin2';
SET collation_server = 'latin2_czech_cs';
```

### 在 Database 层级设置字符集和校对规则

`CREATE DATABASE` 和 `ALTER DATABASE` 语句 (statement) 拥有可选的字符集和校对规则字句（款项, clause）。如果省略这些子句，将使用服务器默认值。因此，我们可以在创建数据库的时候显式指定字符集和校对规则；也可以通过 `ALTER DATABASE`来更改数据库的字符集和校对规则。例如：

```SQL
CREATE DATABASE test_db
    CHARACTER SET = 'utf8mb3'
    COLLATE = 'utf8mb3_general_ci';

ALTER DATABASE test_db COLLATE = 'utf8mb3_unicode_ci';
```

### 在 TABLE 层级设置字符集和校对规则

### 在 COLUMN 层级设置字符集和校对规则

