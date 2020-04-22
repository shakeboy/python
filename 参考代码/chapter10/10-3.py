x,y = eval(input("请输入两个整数: "))
try:
  z = x / y
  print("z =",z)
except TypeError as e1:
  print("数据类型错误:",e1)
except ZeroDivisionError:
  print("除数为零错误!")
except:
  print("程序运行异常!")
else:
  print("程序执行正确！")
