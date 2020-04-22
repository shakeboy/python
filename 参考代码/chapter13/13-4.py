from multiprocessing import Process,Queue
import os,time,random
#写Queue函数.
def writeQueue(q):
  n = random.randint(1,100)
  print("放入Queue中的数据为:",n)
  q.put(n)	#向Queue写数据.
  time.sleep(1) 	#休眠1秒.
#读Queue函数.
def readQueue(q):
  #print('读Queue进程. ID = %s' % os.getpid())
  d = q.get(True)     	#从Queue读数据.
  print("从Queue中读取数据为:",d)	#输出从Queue读取的数据.
if __name__== '__main__':
  q = Queue()  	#创建队列对象q.
  spw = Process(target=writeQueue,args=(q,))   	#创建子进程spw.
  spr = Process(target=readQueue,args=(q,))    	#创建子进程spr.
  spw.start()    	#启动子进程spw.
  spr.start()     	#启动子进程spr.
  spw.join()
  spr.join()
