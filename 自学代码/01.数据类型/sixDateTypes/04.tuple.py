# 元组是有序且不可更改的集合。在 Python 中，元组是用圆括号编写的。
tuple0 = (1, 2, 3, 4, 5)
# 访问元组项目
# 您可以通过引用方括号内的索引号来访问元组项目：
print(tuple0[2])
# 负索引
# 负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目，依此类推。
print(tuple0[-5:-1])
# 创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。
#
# 但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组
tuple0 = list(tuple0)
tuple0[0] = "我是通过转换成列表来修改我的元素"
tuple0 = tuple(tuple0)
print(tuple0)
# 遍历元组
for i in tuple0:
    print(i)
# len()元组长度
print("\n", len(tuple0))

# 元组一旦创建，您就无法向其添加项目。元组是不可改变的。
# 单项元组，别忘了逗号：
print(type(tuple0))
tuple1 = ("apple",)
print(type(tuple1))

# 不是元组
notATuple = ("apple")  # Remove redundant parentheses
print(type(notATuple))
# 您无法删除元组中的项目。
#
# 元组是不可更改的，因此您无法从中删除项目，但您可以完全删除元组：
del tuple0
# 合并两个元组
tu1 = (1, 2)
tu2 = (3, 4, 5)
print(tu1 + tu2)
"""
tuple() 构造函数
也可以使用 tuple() 构造函数来创建元组。
"""
thistuple = tuple(("apple", "banana", "cherry"))  # 请注意双括号
print(thistuple)
print(tu1.index(2))  # 在元组中搜索指定的值并返回找到它的位置
print(tu1.count(1))  #返回元组中指定值出现的次数
