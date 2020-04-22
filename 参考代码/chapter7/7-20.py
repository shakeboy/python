import timeit
def myFun():
  sum = 0
  for i in range(1,100):
    for j in range(1,100):
      sum = sum + i * j
t1 = timeit.timeit(stmt=myFun,number=1000)            #执行代码1000次.
print("t1:",t1)
t2 = timeit.repeat(stmt=myFun,number=1000,repeat=6) #执行代码1000次，重复6遍.
print("t2:",t2)
