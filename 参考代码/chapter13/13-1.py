from multiprocessing import Process
import os
#定义函数.
def spFunc(spName):
  print('子进程标识: %s, ID: %s.' % (spName,os.getpid()))	#查看子进程标识和ID.
if __name__ == '__main__':
  print('主进程开始...')
  print('主进程ID: %s.' % os.getpid())	#查看主进程ID.
  sp1 = Process(target=spFunc,args=('sp1',))	#创建子进程sp1.
  sp2 = Process(target=spFunc,args=('sp2',))	#创建子进程sp2.
  sp1.start()    	#启动子进程sp1.
  sp2.start()    	#启动子进程sp2.
  sp1.join()     	#sp1进入阻塞状态.
  sp2.join()     	#sp2进入阻塞状态.
  print('主进程结束.')
