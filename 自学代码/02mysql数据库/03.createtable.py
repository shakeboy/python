import mysql.connector

conndb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor = conndb.cursor()
createtablesql = "create table mytable(name varchar(10) primary key not null,age int(5) not null)"
mycursor.execute(createtablesql)

