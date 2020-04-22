from fractions import Fraction
a = Fraction(2,5)           		#创建分数对象.
b = Fraction(1,5)                     #创建分数对象.
print(a.denominator)              			#查看分母.
print(a.numerator)                			#查看分子.
print(a + b)                      			#分数之间的算术运算.
from fractions import Decimal
print(1 / 3)                       			#一般精度实数.
print(Decimal(1 / 3))               		#高精度实数.
