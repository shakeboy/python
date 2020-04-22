import multiprocessing
#定义函数.
def spFunc(num):
  for i in range(3):
    num[i] = num[i] ** 3                           #子进程修改num.
if __name__ == "__main__":
  num = multiprocessing.Array("i",[1,3,5])     #创建num对象.
  print("初始数组:",num[:])
  sp = multiprocessing.Process(target=spFunc,args=(num,))  #创建子进程sp.
  sp.start()   #启动子进程sp.
  sp.join()
  print("子进程修改后的数组:",num[:])
