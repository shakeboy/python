#定义求斐波那契数列第n项的函数.
def fib(n):
  if n == 1 or n == 2:
   return 1
  else:
   return fib(n - 1) + fib(n - 2)
#求斐波那契数列前20项目之和.
sum = 0
for i in range(1,21):
  sum = sum + fib(i)
print("前20项之和为:",sum)
