import threading,queue,time
#定义线程类.
class MyThread(threading.Thread):
  #重写构造方法.
  def __init__(self,q,i):
    super(MyThread,self).__init__()
    self.q = q
    self.i = i
  #重写run()方法.
  def run(self):
    self.q.put("这是第 %d 个线程 …" % (self.i))     	#向q中写数据.
if __name__ == '__main__':
  q = queue.Queue()    	#创建队列.
  #创建3个子线程并启动.
  for i in range(3):
    MyThread(q,i).start()
  #输出队列q中的内容.
  while not q.empty():
    print(q.get()) 	#从q中读数据.
