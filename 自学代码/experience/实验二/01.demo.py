# 1．编写一个程序，完成以下功能：
# (1)使用input()函数从键盘输入3个浮点数作为长方体的棱长。
# (2)计算并输出长方体的体积和表面积。
# import math


print("请输入第一个数：")
a = float(input())
print("请输入第二个数：")
b = float(input())
print("请输入第三个数：")
c = float(input())
print("长方体的体积是：")
print(a*b*c)
print("长方体的面积是：")
print(2*a*b + 2*a*c + 2*b*c)


