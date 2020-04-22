import math

a = 2.0                          			#二次项系数.
b = 3.0                          			#一次项系数.
c = 1.0                          			#常数项.
pbs = b ** 2 - 4 * a * c             	#计算判别式的大小.
x1 = (-b + math.sqrt(pbs)) / (2 * a)	#计算第1个根.
x2 = (-b - math.sqrt(pbs)) / (2 * a)	#计算第2个根.
print("x1 =",x1)
print("x2 =",x2)
