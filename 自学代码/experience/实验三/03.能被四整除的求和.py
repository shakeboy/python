
print("输入两个数，求范围内能被四整除的所有数的和")
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
result = 0
for num in range(a, b+1):
    if num % 4 == 0:
        print(num)
        result += num
print("所有数的和为：", result)