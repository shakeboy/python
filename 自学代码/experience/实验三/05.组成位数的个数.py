"""
1,简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(100 * i + 10 * j + k)
"""
2,简述：这里有四个数字，分别是：1,0,3,9,5,7
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
print("\n")
count = 0
tup = [1, 3, 9, 5, 7]
for i in tup:
    for j in tup:
        for k in tup:
            if i != j and i != k and j != k and i != 0:
                print(100 * i + 10 * j + k)
                count += 1
print()
print(count)