import abc
import math


class shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getArea(self):
        pass

    @abc.abstractmethod
    def getPerimeter(self):
        pass


class Triangle(shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        p = (self.a + self.b + self.c) / 2
        S = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print("三角形的面积为：", S)

    def getPerimeter(self):
        C = self.a + self.b + self.c
        print("三角形的周长为：", C)


class Rectangle(shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        S = self.a * self.b
        print("矩形的面积为：", S)

    def getPerimeter(self):
        C = (self.a + self.b) * 2
        print("矩形的周长为：", C)


class Circle(shape):
    def __init__(self, r):
        self.r = r

    def getArea(self):
        S = 3.14 * self.r * self.r
        print("圆形的面积为：", S)

    def getPerimeter(self):
        C = 3.14 * self.r * 2
        print("圆形的周长为：", C)


tri = Triangle(7, 8, 9)
tri.getArea()
tri.getPerimeter()

rec = Rectangle(5, 6)
rec.getArea()
rec.getPerimeter()

cir = Circle(4)
cir.getArea()
cir.getPerimeter()
