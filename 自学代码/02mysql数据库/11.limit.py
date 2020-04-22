# 您可以使用 "LIMIT" 语句限制从查询返回的记录数：
import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
sql = "select * from mytable limit 10"
mycursor.execute(sql)
# 注释：我们用了 fetchall() 方法，该方法从最后执行的语句中获取所有行。
result = mycursor.fetchall()
# for i in result:
#     print(i)
# 选取列
# 如需只选择表中的某些列，请使用 "SELECT" 语句，后跟列名：
# 从另一个位置开始
# 如果希望从第三条记录开始返回五条记录，您可以使用 "OFFSET" 关键字：
# 从位置三开始返回5条数据
mycursor.execute("select name from mytable limit 5 offset 2")
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

