# 水仙花数是指一个3位数，它的每个位上的数字的3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
print("水仙花数有：")
for num in range(100, 1000):
    s = str(num)
    a = int(s[-1])
    b = int(s[-2])
    c = int(s[-3])
    if num == a ** 3 + b ** 3 + c ** 3:
        print(num)
