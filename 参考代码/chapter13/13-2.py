import os,time
from multiprocessing import Process
#创建Process类的派生类.
class SubProcess(Process):
  #构造方法.
  def __init__(self):
    Process.__init__(self)
  #重写run()方法.
  def run(self):
    print("子进程名称 = {0}, ID = {1}".format(self.name,self.pid))
    time.sleep(2)
if __name__ == '__main__':
  print("主进程开始...")
  for i in range(3):
    sp = SubProcess() 					#创建多个进程.
    sp.start()
    sp.join()
  print("主进程结束.")
