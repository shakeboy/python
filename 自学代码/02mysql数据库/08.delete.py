"""
删除记录
您可以使用 "DELETE FROM" 语句从已有的表中删除记录：
"""
import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
sql = "delete from mytable where id >20"
mycursor.execute(sql)
conndb.commit()
print()
print(mycursor.rowcount, "record(s) deleted")
"""
重要：请注意语句 mydb.commit()。需要进行更改，否则表不会有任何改变。

请注意 DELETE 语法中的 WHERE 子句：WHERE 子句指定应删除哪些记录。如果省略 WHERE 子句，则将删除所有记录！
"""
"""
模糊删除
"""
sql1 = "DELETE FROM mytable WHERE name like '%l'"
mycursor.execute(sql1)
conndb.commit()
print()
print(mycursor.rowcount, "record(s) deleted")
"""
防止 SQL 注入
在 delete 语句中，转义任何查询的值也是一种好习惯。
此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
mysql.connector 模块使用占位符 ％s 来转义 delete 语句中的值："""
sql2 = "delete from mytable where name = %s"
var = ("石义钊",)  # 写成元组的形式，不是字符串的形式，占位符
mycursor.execute(sql2, var)
conndb.commit()
print(mycursor.rowcount, "record(s) deleted")

