#定义函数.
def Swap(x,y):                                  	#2个形参:x，y.
   print("交换前：x = %d, y = %d"%(x,y))
   x,y = y,x                                   	#交换2个形参x、y的值.
   print("交换后：x = %d, y = %d"%(x,y))
a = 5; b = 6                                    #定义变量a，b.
print("调用前：a = %d, b = %d."%(a,b))
Swap(a,b)                                        #调用函数Swap().
print("调用后：a = %d, b =%d."%(a,b))
