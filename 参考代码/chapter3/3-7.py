x,op,y = input("请输入操作数和操作符: ").split() 	#输入时各部分之间使用空格分隔.
if op == "+":                                        #加法运算.
  z = float(x) + float(y)
  print("运行结果:",x,op,y,"=",z)
elif op == "-":                                      #减法运算.
  z = float(x) - float(y)
  print("运行结果:",x,op,y,"=",z)
elif op == "*":                                      #乘法运算.
  z = float(x) * float(y)
  print("运行结果:",x,op,y,"=",z)
elif op == "/":                                      #除加法运算.
  z = float(x) / float(y)
  print("运行结果:",x,op,y,"=",z)
else:
  print("您输入的运算符不支持!请重新输入！")
