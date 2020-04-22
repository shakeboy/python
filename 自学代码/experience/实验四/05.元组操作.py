import random

list = []
tuple()
for i in range(20):
    item = random.randint(0, 11)
    list.append(item)
tu = tuple(list)
print('生成20个随机整数的列表为：', tu)
for i in range(1, 11):
    count = tu.count(i)
    print("整数" + str(i) + "在元组中出现的次数为" + str(count) + "次")
