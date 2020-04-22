# 更新表
# 您可以使用 "UPDATE" 语句来更新表中的现有记录：
import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
mycursor.execute("update mytable set name='小清新' where age<20")
conndb.commit()
print(mycursor.rowcount, "行受影响")
conndb.close()
"""
重要：请注意语句 mydb.commit()。需要进行更改，否则不会表不会有任何改变。
请注意 UPDATE 语法中的 WHERE 子句：WHERE 子句指定应更新的记录。如果省略 WHERE 子句，则所有记录都将更新！
"""
"""
防止 SQL 注入
在 update 语句中，转义任何查询的值都是个好习惯。
此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
mysql.connector 模块使用占位符 ％s 来转义 delete 语句中的值：
"""
sql1 = "update mytable set name=%s where age=%s"
