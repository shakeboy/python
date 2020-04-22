# 4、判断并输出100—1000之间的所有素数。
list1 = []
for i in range(100, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list1.append(i)
n = 10  # 每10个数换一行
print("100—1000之间的所有素数:")
for i in range(len(list1)):
    print(list1[i], end='===')
    if (i + 1) % 10 == 0:
        print("")
