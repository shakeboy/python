import math               						#导入模块.
#定义函数.
def func(x,y):
  z = math.sqrt(x ** 2 + y ** 2 )
  return z
if __name__ == "__main__":
  a = int(input("请输入一个整数："))         #定义变量a.
  b = int(input("请输入一个整数："))         #定义变量b.
  c = func(a,b)             				  #调用func()函数，结果赋给变量c.
  print("c =",c)          			       #输出.
