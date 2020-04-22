def outerFunc():
  x = 100                            	#创建闭包变量x.
  def innerFunc():
    nonlocal x                        	#使用关键字nonlocal修改x为闭包变量.
    print("闭包变量: x =",x)
    x = 200                            #修改闭包变量的值.
    print("修改后的闭包变量: x =",x)
  innerFunc()
outerFunc()                           	#调用外函数.
