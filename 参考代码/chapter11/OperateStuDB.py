import pymysql

#定义操作数据库类.
class OperateStuDB:
  #构造方法.
  def __init__(self):
    try:
      self.conn = pymysql.connect("localhost","root","123456","StuDB",3306)
      self.cur = self.conn.cursor()
      #查询指定数据表table_stu是否存在.不存在，则创建.
      sql="SELECT count(*) FROM information_schema.TABLES WHERE table_name = 'table_stu'"
      cur1=self.cur.execute(sql)
      if self.cur.fetchone()[0]==0:	#表不存在，创建新表.
        sql = "create table if not exists StuDB.table_stu(Sno char(20) primary key," "Sname char(20),Sex char(1),Age int)"
        self.cur.execute(sql)
        self.conn.commit()
        print("创建数据表成功！")
    except Exception as e:
      print("创建数据表失败:",e)
  #添加记录.
  def add_record(self,sql,param):
    try:
      self.cur.executemany(sql,param) 	#添加多条记录.
      self.conn.commit()
    except Exception as e:
      raise e
  #查询记录.
  def select_record(self,sql,param):
    try:
      self.cur.execute(sql,param)
      return self.cur
    except Exception as e:
      raise e
  #更新记录.
  def update_record(self,sql,param):
    try:
      self.cur.execute(sql,param)
      self.conn.commit()
    except Exception as e:
      raise e
  #删除记录.
  def delete_record(self,sql,param):
    try:
      self.cur.execute(sql,param)
      self.conn.commit()
    except Exception as e:
      raise e
  #析构方法.
  def __del__(self):
    self.cur.close()
    self.conn.close()

if __name__ == '__main__':
  stu = OperateStuDB()  	#创建对象.
  print("1.添加记录:")
  try:
    stuList=[("1001","Smith","m","16"),("1002","Amy","f","15")]	#待添加的数据.
    #该行数据存在则不插入，否则插入表中.
    addsql="replace into table_stu(Sno,Sname,Sex,Age) values(%s,%s,%s,%s)"
    stu.add_record(addsql,stuList)
    print("添加记录成功！")
  except Exception as e:
    print("添加记录失败:",e)
  print("2.查询记录:")
  try:
    param=("10")  	#参数.
    selectsql = "select * from table_stu where Age>=%s"
    cur1 = stu.select_record(selectsql,param)
    for row in cur1.fetchall():
      print(row[0],row[1],row[2],row[3])
  except Exception as e:
    print("查询记录失败:",e)
  print("3.更新记录:")
  try:
    param=("17","1001")  	#参数.
    updatesql = "update table_stu set Age=%s where Sno=%s"
    stu.update_record(updatesql,param)
    print("更新记录成功！")
  except Exception as e:
    print("更新记录失败:",e)
  print("4.删除记录:")
  try:
    param = ('1002')    	#参数.
    deletesql = "delete from table_stu where Sno=%s"
    stu.delete_record(deletesql,param)
    print("删除记录成功！")
  except Exception as e:
    print("删除记录失败:",e)
  print("5.查询记录:")
  try:
    param=("10")
    selectsql = "select * from table_stu where Age>=%s"
    cur1 = stu.select_record(selectsql,param)
    for row in cur1.fetchall():
      print(row[0],row[1],row[2],row[3])
  except Exception as e:
    print("查询记录失败:",e)
  del stu      	#删除对象.
