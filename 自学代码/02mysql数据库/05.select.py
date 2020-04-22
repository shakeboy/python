"""
从表中选取
如需从 MySQL 中的表中进行选择，请使用 "SELECT" 语句：
"""
import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
sql = "select * from mytable"
mycursor.execute(sql)
# 注释：我们用了 fetchall() 方法，该方法从最后执行的语句中获取所有行。
result = mycursor.fetchall()
# for i in result:
#     print(i)
# 选取列
# 如需只选择表中的某些列，请使用 "SELECT" 语句，后跟列名：
mycursor.execute("select name from mytable")
result1 = mycursor.fetchall()
# for i in result1:
#      print(i)
# 使用 fetchone() 方法
# 如果您只对一行感兴趣，可以使用 fetchone() 方法。
#
# fetchone() 方法将返回结果的第一行：
print(result1)
print(result)
mycursor.execute(sql)
result2 = mycursor.fetchone()
print(result2)
