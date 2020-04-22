#定义装饰器.
def deco(func):
  print("I am in deco.")
  func()                                      	#调用函数func().
  return "deco return value."
#使用装饰器修饰函数.
@deco
def func():
  print("I am in func.")
print(func)
