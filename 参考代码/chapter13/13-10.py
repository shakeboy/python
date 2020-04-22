from threading import Thread
import time
#定义函数.
def thFunc(i):
  print("线程 %d 启动 ..."%i)
  time.sleep(1)
if __name__ == '__main__':
  print("主线程开始 ...")
  for i in range(3):
    th = Thread(target=thFunc,args=(i,))   	#创建线程.
    th.start()    	#启动线程.
    th.join()     	#等待线程结束.
  print("主线程结束.")
