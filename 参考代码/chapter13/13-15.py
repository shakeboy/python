import threading,time
#定义函数.
def countFunc(tName ,lock):
    global num;    	#全局变量.
    lock.acquire()  	#加Lock.
    while True:
      if num <= 3:
        print("当前线程是 %s, num = %s." % (tName,num))
        num = num + 1
        time.sleep(1)
      else:
        break
    lock.release()   	#释放Lock.
if __name__ == "__main__":
  num = 1
  lock = threading.Lock()
  t1 = threading.Thread(target=countFunc,args=('A',lock))   	#创建线程t1.
  t2 = threading.Thread(target=countFunc,args=('B',lock))   	#创建线程t2.
  t1.start()    	#启动线程t1.
  t2.start()    	#启动线程t2.
