import math

x = float(input("请输入第一个数:"))
y = float(input("请输入第二个数:"))
z = float(input("请输入第三个数:"))
result = float(3*x + 4*math.sqrt(x**2+2*y**2))/(1+math.cos(z**3))
print("结果为：" + str(result))

