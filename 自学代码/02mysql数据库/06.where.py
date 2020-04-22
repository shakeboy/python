"""
使用筛选器来选取
从表中选择记录时，可以使用 "WHERE" 语句对选择进行筛选：
"""
import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
sql = "select * from mytable where id>90"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

"""
通配符
您也可以选择以给定字母或短语开头、包含或结束的记录。
请使用 ％ 表示通配符：
"""
sql1 = "select * from mytable where name like '%l'"
mycursor.execute(sql1)
result = mycursor.fetchall()
print(result)

"""
防止 SQL 注入
当用户提供查询值时，您应该转义这些值。
此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
mysql.connector 模块拥有转义查询值的方法：
"""
