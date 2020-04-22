# 列表list中包含10个1～100之间的随机整数，将列表list中的奇数变成它的平方，偶数变成它的立方。编程实现上述功能。

import random

li = random.sample(range(1, 101), 10)
li1 = []
print(li)
for i in li:
    if i % 2 != 0:
        i = i ** 2
        li1.append(i)
    else:
        i = i ** 3
        li1.append(i)
print("修改后的列表为：")
print(li1)
