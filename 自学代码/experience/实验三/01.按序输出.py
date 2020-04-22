# 1、从键盘输入三个数，赋给变量a、b、c，按从大到小的顺序输出。
def largeToSmall(a, b, c):
    temp = 0
    if a < b:
        temp = a
        a = b
        b = temp
    if a < c:
        temp = a
        a = c
        c = temp
    if b < c:
        temp = b
        b = c
        c = temp
    print("从大到小顺序依次为：")
    print(a, ' ', b, ' ', c, ' ')


if __name__ == '__main__':
    a = float(input("请输入a:"))
    b = float(input("请输入b:"))
    c = float(input("请输入c:"))
    largeToSmall(a, b, c)
