"""
Python 集合（数组）
Python 编程语言中有四种集合数据类型：
列表（List）是一种有序和可更改的集合。允许重复的成员。
元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
集合（Set）是一个无序和无索引的集合。没有重复的成员。
词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。
选择集合类型时，了解该类型的属性很有用。
为特定数据集选择正确的类型可能意味着保留含义，并且可能意味着提高效率或安全性。
"""
# 列表的表示
# 列表是一个有序且可更改的集合。在 Python 中，列表用方括号编写。
list0 = [1, 2, 3, 4, 5, 6]
print(list0)
print(type(list0))
print(list0[0])
print(list0[-3:-1])
print(list0[2:5])
"""
结果：
[1, 2, 3]
<class 'list'>
1 ==》您可以通过引用索引号来访问列表项：
[1, 2] ==>负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目，依此类推。
[3, 4, 5] ==>list0[2:5]返回3-5项
"""
# 可以改变索引值
list0[2] = "我是索引变过来的"
print(list0)
# 遍历列表
print("我来遍历列表")
for i in list0:
    print(i)
# 检查项目是否含有某一项
if 1 in list0:
    print("1在里面呢")
else:
    print("1不在里面")
# 列表长度
print(len(list0))
# append()添加项目
list0.append([2, 3, 5])
print(list0)
# insert()插入项目
list0.insert(1, ['我是插入的', '我可不一般', 520])
print(list0)
# 删除项目remove()
list0.remove(6)
print(list0)
# pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）：
list0.pop()
print(list0)
list0.pop(0)
print(list0)
# del 关键字删除指定的索引：
del list0[0]
print(list0)
# clear()清空列表
list0.clear()
print(list0)
# del list0 删除列表
print()
"""
复制列表
您只能通过键入 list2 = list1 来复制列表，因为：list2 将只是对 list1 的引用，list1 中所做的更改也将自动在 list2 中进行。
有一些方法可以进行复制，一种方法是使用内置的 List 方法 copy()。
实例
使用 copy() 方法来复制列表：
"""
# 复制列表 直接复制
list0.append([1, 2, 3])
list1 = list0
print(list1)
list2 = list1.copy()
print(list2)
# 制作副本的另一种方法是使用内建的方法 list()。
list3 = ["apple", "banana", "cherry"]
list4 = list(list3)
print(list4)
# 合并两个列表
print(list3 + list1)
# 追加列表
for i in list1:
    list3.append(i)
print(list3)
# 或者，您可以使用 extend() 方法，其目的是将一个列表中的元素添加到另一列表中：
print(list3.extend(list1))
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# list()构造函数
myList = list((5, 2, 3, 4))  # 请注意双括号
print(myList)

"""
一些方法
append() 在列表的末尾添加一个元素 
clear() 删除列表中的所有元素 
copy() 返回列表的副本 
count() 返回具有指定值的元素数量。 
extend() 将列表元素（或任何可迭代的元素）添加到当前列表的末尾 
index() 返回具有指定值的第一个元素的索引 
insert() 在指定位置添加元素 
pop() 删除指定位置的元素 
remove() 删除具有指定值的项目 
reverse() 颠倒列表的顺序 
sort() 对列表进行排序 
"""
myList = [4, 5, 2, 1]
print(sorted(myList))
myList0 = [4, 2, 6, 1]
myList0.sort()
print(myList0)
