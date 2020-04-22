import multiprocessing,time,os
#定义函数.
def spFunc(i):
  print("子进程ID = {}, 结果 = {}.".format(os.getpid(),i ** 2))
  time.sleep(1)
if __name__ == "__main__":
  pool = multiprocessing.Pool(processes=3) 	#进程池pool中可以包含的进程数.
  #创建进程池并启动其中的进程.
  for i in range(1,4):
    pool.apply(spFunc,(i,))
  pool.close()
  pool.join()
