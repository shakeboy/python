from multiprocessing import Process,Lock
import time,os
#子进程将调用函数.
def spFunc(spName,v,lock):
  #lock.acquire()	#加锁.
  for i in range(1,3):
    n = i ** v
    time.sleep(0.5)   	#休眠0.5秒.
    print ("{0}: number = {1}".format(spName,n))
  #lock.release()	#释放锁.
if __name__ == "__main__":
  lock = Lock() 	#创建锁.
  sp1 = Process(target=spFunc,args=("sp1",2,lock))  	#创建子进程sp1.
  sp2 = Process(target=spFunc,args=("sp2",3,lock))  	#创建子进程sp2.
  sp1.start()   	#启动子进程sp1.
  sp2.start()   	#启动子进程sp2.
