# 局部作用域
# 在函数内部创建的变量属于该函数的局部作用域，并且只能在该函数内部使用。
def myfunc():
    x = 100
    print(x)


myfunc()


# 函数内部的函数
# 如上例中所示，变量 x 在函数外部不可用，但对于函数内部的任何函数均可用：
def myfunc():
    x = 100

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# 全局作用域
# 在 Python 代码主体中创建的变量是全局变量，属于全局作用域。
#
# 全局变量在任何范围（全局和局部）中可用。
x = 100


def myfunc():
    print(x)


myfunc()

print(x)

# Global 关键字
"""
如果您需要创建一个全局变量，但被卡在本地作用域内，则可以使用 global 关键字。

global 关键字使变量成为全局变量。

实例"""


def myfunc():
    global x
    x = 100


myfunc()

print(x)
