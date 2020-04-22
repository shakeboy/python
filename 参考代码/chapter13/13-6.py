from multiprocessing import Process,Manager
#定义函数.
def spFunc(dict,list):
  dict['Alice'] = 21
  dict['Beth'] = 22
  list.append("physics")
  list.append("chemistry")
if __name__ == '__main__':
  manager = Manager()     	#创建Manager对象.
  list = manager.list()
  dict = manager.dict()
  sp = Process(target=spFunc,args=(dict,list))
  sp.start()
  sp.join()
  print("list:",list)
  print("dict:",dict)
