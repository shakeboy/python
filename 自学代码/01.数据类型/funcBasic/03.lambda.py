"""
lambda 函数是一种小的匿名函数。
lambda 函数可接受任意数量的参数，但只能有一个表达式。
语法规则：lambda arguments : expression
"""

x = lambda a: a + 156
print(x(1))
x = lambda a, b: a * b
print(x(5, 6))


# lambda和函数的结合使用
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
# 如果在短时间内需要匿名函数，请使用 lambda 函数。
