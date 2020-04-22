import time,threading
#定义线程类.
class MyThread(threading.Thread):
  #重写构造方法.
  def __init__(self):
    threading.Thread.__init__(self)
  #重写run()方法.
  def run(self):
    for i in range(2):
      print("这里是线程 %s 中的 %d."%(self.getName(),i))  #输出返回的线程名称.
      time.sleep(1)
if __name__ == '__main__':
  th1 = MyThread()
  th2 = MyThread()
  th1.setName("线程-1")    			#设置线程名称.
  th2.setName("线程-2")    			#设置线程名称.
  th1.start()
  th2.start()
  th1.join()
  th2.join()
