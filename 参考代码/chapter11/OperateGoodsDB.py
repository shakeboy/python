import pyodbc
import os

#定义操作数据库类.
class OperateGoodsDB:
  #构造方法.
  def __init__(self):
    try:
      self.conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + os.getcwd() + r"\GoodsDB.accdb;Uid=;Pwd=;")
      self.cur = self.conn.cursor()
    except Exception as e:
      print("连接数据库失败:",e)
  #添加记录.
  def add_record(self,sql,param):
    try:
      self.cur.execute(sql,param)
      self.conn.commit()
    except Exception as e:
      raise e
  #查询记录.
  def select_record(self,sql,param):
    try:
      cur1 = self.cur.execute(sql,param)
      return cur1
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
  #查询满足条件的记录数.
  def num_of_record(self,sql,param):
    try:
      cur1 = self.cur.execute(sql,param)
      return cur1.fetchone()[0]   	#获取第1行第1列的数据.
    except Exception as e:
      raise e
  #析构方法.
  def __del__(self):
    self.cur.close()
    self.conn.close()

if __name__ == '__main__':
  goods = OperateGoodsDB()     	#创建对象.
  print("1.添加记录:")
  goodsList = [("1001","长虹电视","家电","四川","1288"),("1002","红富士苹果",
    "水果","日本","16")]        		          #待添加的数据.
  try:
#查询指定名称的商品在表table_goods中是否存在.不存在，则添加到表中.
    for item in goodsList:
      GoodsName=(item[1])
      n=goods.num_of_record("select count(*) from table_goods where GoodsName=?",GoodsName)
      if n==0:
        addsql = "insert into table_goods VALUES(?,?,?,?,?)" 	#使用?作为占位符.
        goods.add_record(addsql,item)
    print("添加记录成功！")
  except Exception as e:
    print("添加记录失败:",e)
  print("2.查询记录:")
  try:
    selectsql = "select * from table_goods"
    param=()  	#空参数.
    cur1 = goods.select_record(selectsql,param)
    for line in cur1.fetchall():
      for item in line:
        print(item,end=' ')
      print()
  except Exception as e:
    print("查询记录失败:",e)
  print("3.更新记录:")
  try:
    param=("888","长虹电视")     	#参数.
    updatesql = "update table_goods set Price=? where GoodsName=?"
    goods.update_record(updatesql,param)
    print("更新记录成功！")
  except Exception as e:
    print("更新记录失败:",e)
  print("4.删除记录:")
  try:
    GoodsName =('红富士苹果')   	#参数.
    deletesql = "delete from table_goods where GoodsName=?"
    goods.delete_record(deletesql,GoodsName)
    print("删除记录成功！")
  except Exception as e:
    print("删除记录失败:",e)
  print("5.查询记录:")
  try:
    selectsql = "select * from table_goods"
    param = ()  	#空参数.
    cur1 = goods.select_record(selectsql,param)
    #遍历结果集中所有数据.
    for line in cur1.fetchall():
      for item in line:
        print(item,end=' ')
  except Exception as e:
    print("查询记录失败:",e)
  del goods     	#删除对象.
