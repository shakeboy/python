set1 = {2, 5, 9, 1, 3}
set2 = {3, 6, 8, 2, 5}
set1.add(7)
print("添加元素7后：", set1)
set4 = set1.union(set2)
print("并集为：", set4)
set3 = set1.intersection(set2)
print("交集为：", set3)
set3 = set1.difference(set2)
print("差集为：", set3)
print("判断给定关键字 key=4是否在 set1 或set2中：", 4 in set4)
