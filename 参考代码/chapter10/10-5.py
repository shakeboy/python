#定义函数.
def greaterZero(n):
  if n < 0:
    raise Exception("您传入了一个小于零的整数！")     	#抛出异常.
  else:
    print("n =",n)
try:
  x = int(input("请输入一个整数: "))
  greaterZero(x) 									#调用函数.
except Exception as e:
  print(e)
