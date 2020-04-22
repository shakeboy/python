import multiprocessing,time
#定义函数.
def sjFunc(event):
  print('接收订单和货款...')
  print('发货...')
  event.set()      #将当前进程设置为True.
  event.clear()    #将当前进程设置为False.
  event.wait()     #阻塞当前进程.
  print('欢迎再次订购!')
#定义函数.
def gkFunc(event):
  print('准备买商品...')
  print('下订单、付款...')
  event.wait()     #阻塞当前进程.
  print('收到商品...')
  print('评价商品...')
  event.set()      #将当前进程设置为True.
  event.clear()    #将当前进程设置为False.
if __name__ == '__main__':
  event = multiprocessing.Event()  #创建event对象.
  sjp = multiprocessing.Process(target=sjFunc,args=(event,))   #创建子进程sjp.
  gkp = multiprocessing.Process(target=gkFunc,args=(event,))   #创建子进程gkp.
  gkp.start()      #启动子进程gkp.
  time.sleep(0.5)      #休眠0.5秒.  #保证gkp线程先启动.
  sjp.start()      #启动子进程sjp.
