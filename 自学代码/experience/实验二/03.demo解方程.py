import math


# a*x**2 + b*x + c  = d
def solveEquation(a, b, c, d):
    if a == 0:
        if b == 0:
            if c == d:
                print("方程恒有解")
            else:
                print("方程无解")
        else:
            print("一次方程解为：x = ", (d - c) / b)
    else:
        if b ** 2 - 4 * a * c < 0:
            print("二次方程无解")
        elif b ** 2 - 4 * a * c == 0:
            print("二次方程的解为:x = ", (-b) / (2 * a))
        else:
            print("两个解：x1 = ", (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            print("两个解：x2 = ", (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))


if __name__ == '__main__':
    while 1:
        a = float(input("请输入a:"))
        b = float(input("请输入b:"))
        c = float(input("请输入c:"))
        d = float(input("请输入d:"))
        solveEquation(a, b, c, d)
