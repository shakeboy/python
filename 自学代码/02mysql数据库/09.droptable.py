# 您可以使用 "DROP TABLE" 语句来删除已有的表：
import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
mycursor.execute("drop table IF EXISTS test")
conndb.commit()
# 只在表存在时删除
# 如果要删除的表已被删除，或者由于任何其他原因不存在，那么可以使用 IF EXISTS 关键字以避免出错。
