"""
Python 是一种面向对象的编程语言。
Python 中的几乎所有东西都是对象，拥有属性和方法。
类（Class）类似对象构造函数，或者是用于创建对象的“蓝图”。
"""


class Persons:
    name = "石义钊"
    age = 21

    @staticmethod
    def speakEnglish():
        print("My dear")


# 创建对象
p = Persons()
# 调用方法和属性
print(p.name)
p.speakEnglish()

"""
__init__() 函数
上面的例子是最简单形式的类和对象，在实际应用程序中并不真正有用。
要理解类的含义，我们必须先了解内置的 __init__() 函数。
所有类都有一个名为 __init__() 的函数，它始终在启动类时执行。
使用 __init__() 函数将值赋给对象属性，或者在创建对象时需要执行的其他操作：
注释：每次使用类创建新对象时，都会自动调用 __init__() 函数。

对象方法
对象也可以包含方法。对象中的方法是属于该对象的函数。
让我们在 Person 类中创建方法：

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Bill", 63)

print(p1.name)
print(p1.age)
"""
self 参数
self 参数是对类的当前实例的引用，用于访问属于该类的变量。
它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数：
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Bill", 63)
p1.myfunc()
