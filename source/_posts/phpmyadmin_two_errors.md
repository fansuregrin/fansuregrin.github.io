---
title: 使用phpmyadmin访问数据库时，出现的两种警告如何解决
date: '2020-11-27 22:17:00'
categories:
  - - linux
---
我在使用phpmyadmin访问MySQL数据库时，发现了两个警告。

> 现在更新后没有这个bug了！！！

## 551警告

其中一个是点击`导入`和`导出`选项时，浏览器会跳出警告，警告内容如下：

```
in ./libraries/plugin_interface.lib.php#551
count(): Parameter must be an array or an object that implements Countable

Backtrace

./libraries/display_import.lib.php#371: PMA_pluginGetOptions(
string 'Import',
array,
)
./libraries/display_import.lib.php#456: PMA_getHtmlForImportOptionsFormat(array)
./libraries/display_import.lib.php#691: PMA_getHtmlForImport(
string '5bdb3279a72ae',
string 'database',
string 'chihenne',
string '',
integer 16777216,
array,
NULL,
NULL,
string '',
)
./db_import.php#43: PMA_getImportDisplay(
string 'database',
string 'chihenne',
string '',
integer 16777216,
)
```

解决办法是，修改`/usr/share/phpmyadmin/libraries/plugin_interface.lib.php`的第`551`行，原来显示的是`if (! is_null($options) && count($options) > 0) {`, 现在我们把它改为`if ($options != null) {`即可！

## 613警告

另外一个警告是点击数据库中的表时，会弹出一个警告，内容如下：

```
Warning in ./libraries/sql.lib.php#613
count(): Parameter must be an array or an object that implements Countable

Backtrace

./libraries/sql.lib.php#2128: PMA_isRememberSortingOrder(array)
./libraries/sql.lib.php#2079: PMA_executeQueryAndGetQueryResponse
...
```

解决办法是，修改`/usr/share/phpmyadmin/libraries/sql.lib.php`的第`613`行，原来显示的是`|| (count($analyzed_sql_results['select_expr'] == 1)`, 改为`|| ((count($analyzed_sql_results['select_expr']) == 1)`即可！

