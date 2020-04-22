import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
)

# 创建数据库
# 如需在 MySQL 中创建数据库，请使用 "CREATE DATABASE" 语句：
# 创建一个游标，执行语句
cursor = conn.cursor()
"""Instantiates and returns a cursor

        This method is similar to MySQLConnection.cursor() except that
        it checks whether the connection is available and raises
        an InterfaceError when not.

        cursor_class argument is not supported and will raise a
        NotSupportedError exception.

        Returns a MySQLCursor or subclass.
        """
# st = "CREATE DATABASE mydb"
# cursor.execute(st)

st1 = "show databases"
# 检查数据库是否存在
cursor.execute(st1)
for i in cursor:
    print(i)
"""
result:
('information_schema',)
('mydb',)
('mysql',)
('performance_schema',)
('test',)
"""

# 连接指定数据库
conndb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mydb1"
)
print(conndb)
"""
如果数据库不存在，会收到错误。
mysql.connector.errors.ProgrammingError: 1044 (42000): Access denied for user ''@'localhost' to database 'mydb'
"""