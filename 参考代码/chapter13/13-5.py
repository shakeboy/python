from multiprocessing import Pipe,Process
#定义函数.
def spFunc(cPipe):
  while True:
    try:
      print("接收的信息: ",cPipe.recv())
    except EOFError:
      break
if __name__ == '__main__':
  parentPipe,childPipe = Pipe(True)     	#创建管道.
  sp = Process(target=spFunc,args=(childPipe,)) 	#创建子进程sp.
  sp.start()    	#启动子进程sp.
  parentPipe.send("量子通信")     	#发送信息.
  parentPipe.send("引力波") 	#发送信息.
  parentPipe.close()
  sp.join()
