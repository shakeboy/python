# 1．使用两种方法将两个列表中的数据合并。
li1 = [1, 2, 3, 4, 5]
li2 = [3, 4, 5, 6, 8]
# 方法一
li3 = li1 + li2
print(li3)
print("=====================")
li2.extend(li1)
print(li2)