# 1.下载安装包：python -m pip install mysql-connector
# 2.检查是否下载成功:import mysql.connector

import mysql.connector
# 创建数据库连接对象
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(mydb)