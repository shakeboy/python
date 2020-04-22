import threading,time
#子线程调用函数.
def thFunc1(thName,cond):
  with cond:
    for i in range(0,6,2):
      print("线程%s: %d."%(thName,i))
      cond.wait() #等待.
      cond.notify() #通知其它线程.
#线程将执行函数.
def thFunc2(thName,cond):
  with cond:
    for i in range(1,6,2):
      print("线程%s: %d." % (thName,i))
      cond.notify() #通知其它线程.
      cond.wait()#等待.
if __name__ == "__main__":
  cond = threading.Condition()       #创建condtion对象.
  #创建线程th1、th2.
  th1 = threading.Thread(target=thFunc1,args=("th1",cond))
  th2 = threading.Thread(target=thFunc2,args=("th2",cond))
  th1.start()
  th2.start()
  th1.join()
  th2.join()
