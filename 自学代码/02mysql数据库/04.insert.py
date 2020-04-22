import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb1"
)
mycursor = conndb.cursor()
insertsql = "Insert into mytable(name,age)values('是',21)"
# 重要：请注意语句 mydb.commit()。需要进行更改，否则表不会有任何改变
conndb.commit()
mycursor.execute(insertsql)
print(mycursor.rowcount, "record inserted.")
# 要在表中插入多行，请使用 executemany() 方法。
sql = "INSERT INTO mytable (name, age) VALUES (%s ,%s)"
val = [
  ('Peter', 9),
  ('Amy', 10),
  ('Hannah', 40),
  ('Michael', 20),
  ('Sandy', 16),
  ('Betty', 19),
  ('Richard', 25),
  ('Susan', 18),
  ('Vicky', 55),
  ('Ben', 99),
  ('William', 20),
  ('Chuck', 36),
  ('Viola', 45)
]
mycursor.executemany(sql, val)
conndb.commit()
"""
获取已插入 ID
您可以通过询问 cursor 对象来获取刚插入的行的 id。
注释：如果插入不止一行，则返回最后插入行的 id。
"""
print(mycursor.lastrowid)
print(mycursor.rowcount, "record inserted.")
