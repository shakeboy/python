"""
Python 继承
继承允许我们定义继承另一个类的所有方法和属性的类。
父类是继承的类，也称为基类。
子类是从另一个类继承的类，也称为派生类。
"""


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# 使用 Person 来创建对象，然后执行 printname 方法：

x = Person("Bill", "Gates")
x.printname()


class Student(Person):
    pass


s = Student("石义钊", "shakeboy")
s.printname()
s.printname()


# 当您添加 __init__() 函数时，子类将不再继承父的 __init__() 函数。
#
# 注释：子的 __init__() 函数会覆盖对父的 __init__() 函数的继承。
#
# 如需保持父的 __init__() 函数的继承，请添加对父的 __init__() 函数的调用：

# 使用 super() 函数
# Python 还有一个 super() 函数，它会使子类从其父继承所有方法和属性：
