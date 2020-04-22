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
sql = "select * from mytable order by age DESC"
mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)

