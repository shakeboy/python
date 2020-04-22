list = [1, 2, 4, 2, 3, 6, 7, 7, 8, 9]
list.sort()
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
print("删除重复元素后的列表为：", list1)
