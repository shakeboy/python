"""
某个公司采用公用电话传递4位整数数据，该数据在传递过程中是加密的。
加密规则如下：每位数字都加上5，然后用得到的和除以10的余数代替该数字，
再将第1位和第4位交换，第2位和第3位交换。编写程序实现上述功能。
"""
x = int(input("请输入四位整数"))
print("第一阶段")
a = int(x / 1000 + 5) % 10
b = int(x / 100 % 10 + 5) % 10
c = int(x % 100 / 10 + 5) % 10
d = int(x % 10 + 5) % 10
x = int(a*1000 + b*100 + c*10 + d) % 10

print("第二阶段")
x = d*1000 + c*100 + b*10 + a
print("加密后数值为:", x)
