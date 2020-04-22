import pymongo

#数据库类.
class OperateUniDB:
  #构造方法.
  def __init__(self):
    try:
      self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
      self.mydb = self.myclient["UniDB"]
      self.mycol = self.mydb["Unis"]
      #在字段Name上创建唯一索引.
      self.mycol.create_index([("Name",1)],unique=True)
      print("创建/连接数据库和创建集合成功！")
    except Exception as e:
      print("创建数据库和集合失败:",e)
  #添加文档.
  def add_document(self,unis):
    try:
      self.mycol.insert_many(unis)
    except Exception as e:
      raise e
  #查找文档.
  def find_document(self,cons):
    try:
      res = self.mycol.find(cons)
      return res
    except Exception as e:
      raise e
  #更新文档.
  def update_document(self,cons,newvalue):
    try:
      self.mycol.update_many(cons,newvalue)
    except Exception as e:
      raise e
  #删除文档.
  def delete_document(self,cons):
    try:
      self.mycol.delete_many(cons)
    except Exception as e:
      raise e
  #析构方法.
  def __del__(self):
    self.myclient.close()     	#关闭连接.

if __name__ == '__main__':
  uni = OperateUniDB()     	#创建对象.
  print("1.添加文档:")
  unis = [{"Name": "哈佛大学","Nation": "美国","score": 100}, \
          {"Name": "麻省理工大学","Nation": "美国","score": 97.6}, \
          {"Name": "斯坦福大学","Nation": "美国","score": 93.8}, \
          {"Name": "牛津大学","Nation": "英国","score": 87.6}]
  try:
    uni.add_document(unis)
    print("添加文档成功！")
  except Exception as e:
    print("添加文档失败:",e)
  print("2.查询文档:")
  try:
    cons = {"Name":"哈佛大学"}
    res = uni.find_document(cons)
    for item in res:
      print(item)
  except Exception as e:
    print("查询文档失败:",e)
  print("3.更新文档:")
  try:
    cons = {"score":93.8}
    value = {"$set": {"score": 95.8}}
    uni.update_document(cons,value)
    print("更新文档成功！")
  except Exception as e:
    print("更新文档失败:",e)
  print("4.删除文档:")
  try:
    cons = {"Name":"哈佛大学"}
    uni.delete_document(cons)
    print("删除文档成功！")
  except Exception as e:
    print("删除文档失败:",e)
  print("5.查询文档:")
  try:
    param = {}
    res = uni.find_document(param)
    for item in res:
      print(item)
  except Exception as e:
    print("查询文档失败:",e)
  del uni        	#删除对象.
