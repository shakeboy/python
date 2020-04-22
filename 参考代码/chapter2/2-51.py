import math

PI = math.pi                    				#定义圆周率常量.
r = float(input("请输入圆锥体的半径: "))
h = float(input("请输入圆锥体的高: "))
s1 = PI * r ** 2                  			#计算圆锥椎底面积.
s2 = PI * r * math.sqrt(r ** 2 + h ** 2) 	#计算圆锥椎侧面积.
s = s1 + s2                     				#计算圆锥椎表面积.
v = 1/3 * PI * r ** 2 * h            		#计算圆锥椎体积.
print("圆锥体的表面积为: %6.2f"%s)
print("圆锥体的体积为: %6.2f"%v)
