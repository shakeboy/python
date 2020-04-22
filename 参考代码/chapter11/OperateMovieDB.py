import sqlite3

#操作数据库类.
class OperateMovieDB:
  #构造方法.
  def __init__(self):
    try:
      self.conn = sqlite3.connect('MovieDB.db')  	#创建或连接数据库.
      self.cur = self.conn.cursor()
      self.cur.execute('''create table if not exists table_movie(ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text not null,Nation text,Category text,ProductionTime Text,TicketPrice real);''')
      self.conn.commit()
    except Exception as e:
      print("创建/连接数据库或创建数据表失败:",e)
  #添加记录.
  def add_record(self,sql):
    try:
      self.cur.execute(sql)
      self.conn.commit()
    except Exception as e:
      raise e
  #查询记录.
  def select_record(self,sql):
    try:
      cur1 = self.cur.execute(sql)
      return cur1
    except Exception as e:
      raise e
  #更新记录.
  def update_record(self,sql):
    try:
      self.cur.execute(sql)
      self.conn.commit()
    except Exception as e:
      raise e
  #删除记录.
  def delete_record(self,sql):
    try:
      self.cur.execute(sql)
      self.conn.commit()
    except Exception as e:
      raise e
  #查询满足条件的记录数.
  def num_of_record(self,sql):
    try:
      cur1 = self.cur.execute(sql)
      for row in cur1:
        return row[0]
    except Exception as e:
      raise e
  #析构方法.
  def __del__(self):
    self.cur.close()
    self.conn.close()

if __name__ == '__main__':
  movie = OperateMovieDB()    	#创建对象.
  print("1.添加记录:")
  movieList = [["这个杀手不太冷","法国","犯罪","1994",36],["阿甘正传","美国","爱情",
    "1994",37],["我不是药神","中国","搞笑","2018",38]]	#待添加的数据.
  try:
    for item in movieList:
      #如果要添加的电影在数据表table_movie中不存在，则添加.否则，不添加。
      n=movie.num_of_record("select count(*) from table_movie where Name='"+
 	   item[0] +"'")
      if n == 0:
        addsql = "insert into table_movie(Name,Nation,Category,ProductionTime,TicketPrice) VALUES ('"+item[0]+"','"+item[1]+"','"+item[2]+"','"+ item[3]+"',"+str(item[4])+")"
        movie.add_record(addsql)
    print("添加记录成功！")
  except Exception as e:
    print("添加记录失败:",e)
  print("2.查询记录:")
  try:
    selectsql = "select * from table_movie"
    cur1 = movie.select_record(selectsql)
    for row in cur1:
      print("编号:%s,名称:%s,国家:%s,类型:%s,出品时间:%s,票价:%6.2f元." % (row[0],
 	   row[1],row[2],row[3],row[4],row[5]))
  except Exception as e:
    print("查询记录失败:",e)
  print("3.更新记录:")
  try:
    updatesql = "update table_movie set TicketPrice=35 where Name='这个杀手不太冷'"
    movie.update_record(updatesql)
    print("更新记录成功！")
  except Exception as e:
    print("更新记录失败:",e)
  print("4.删除记录:")
  try:
    deletesql = "delete from table_movie where TicketPrice>=38"
    movie.delete_record(deletesql)
    print("删除记录成功！")
  except Exception as e:
    print("删除记录失败:",e)
  print("5.查询记录:")
  try:
    selectsql = "select * from table_movie"
    cur1 = movie.select_record(selectsql)
    for row in cur1:
      print("编号:%s,名称:%s,国家:%s,类型:%s,出品时间:%s,票价:%6.2f元." % (row[0],
 	   row[1],row[2],row[3],row[4],row[5]))
  except Exception as e:
    print("查询记录失败:",e)
  del movie 	#删除对象.
