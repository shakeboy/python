x = 100                                        	#创建全局变量.
def myFunc():
  global x                                   	#使用关键字global修改x为全局变量.
  print("全局变量: x =",x)
  x = 200                                     	#修改全局变量.
  print("修改后的全局变量: x =",x)
myFunc()                                          #调用函数.
