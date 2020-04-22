
x = int(input("请输入一个五位数以内的整数"))
a = int(x / 10000)
b = int(x / 1000 % 10)
c = int(x / 100 % 10)
d = int(x % 100 / 10)
e = int(x % 10)
if a != 0:
    n = 5
    print("五位数")
elif b != 0:
    n = 4
    print("四位数")
elif c != 0:
    n = 3
    print("三位数")
elif d != 0:
    n = 2
    print("二位数")
elif e != 0:
    n = 1
    print("一位数")
else:
    n = 0
    print("零位数")

if n == 1:
    print(e)
elif n == 2:
    print(e, d)
elif n == 3:
    print(e, d, c)
elif n == 4:
    print(e, d, c, b)
else:
    print(e, d, c, b, a)

