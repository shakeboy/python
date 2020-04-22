"""
python有三种数字类型
int ==》Int 或整数是完整的数字，正数或负数，没有小数，长度不限。
float ==》浮动或“浮点数”是包含小数的正数或负数。浮点数也可以是带有“e”的科学数字，表示 10 的幂。
complex ==》复数用 "j" 作为虚部编写：

类型转换
您可以使用 int()、float() 和 complex() 方法从一种类型转换为另一种类型：

"""
import random
# 一、type判断数据类型
print(type(4))
print(type(4.2))
print(type(4 + 5j))
"""
结果：
<class 'int'>
<class 'float'>
<class 'complex'>
"""
# 二、类型转换
# 1.整数转换成浮点数
a = 4
print(type(a))
a = float(a)
print(type(a))
# 2.浮点数转换成复数
a = complex(a)
print(a)
print(type(a))
print(complex(4.5))
# 3.整数转换成浮点数
b = 4
print(complex(b))
# 4.浮点数转换成整数,不会四舍五入
c = 4.2
print(int(c))
print(int(5.9))
# 三、random库
print(random.randrange(1, 40))
