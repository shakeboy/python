"""
集合（Set）
集合是无序和无索引的集合。在 Python 中，集合用花括号编写。

集合是无序的，因此您无法确定项目的显示顺序。

访问项目
您无法通过引用索引来访问 set 中的项目，因为 set 是无序的，项目没有索引。

但是您可以使用 for 循环遍历 set 项目，或者使用 in 关键字查询集合中是否存在指定值。


"""

"""
s0 = {"我是集合", 4, [1, 2, 3]}
print(s0)  # TypeError: unhashable type: 'list'
"""

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1)
# 遍历
for i in s1:
    print(i)
print("\n")
# 添加一个元素
s1.add(14)
print(s1)
# 添加一些元素
s1.update([12, 36, 65, 89])
print(s1)
# 获取长度
print(len(s1))
# 删除项目
s1.remove(12)  # 如果要删除的项目不存在，则 remove() 将引发错误。
print(s1)
s1.discard(1)  # 如果要删除的项目不存在，则 discard() 将引发错误。
print(s1)
a = s1.pop()
# 您还可以使用 pop() 方法删除项目，但此方法将删除最后一项。请记住，set 是无序的，因此您不会知道被删除的是什么项目。
# pop() 方法的返回值是被删除的项目。
print(a)
print(s1)
# union联合集合 ,update也可以，会删除重复项
"""
注释：union() 和 update() 都将排除任何重复项。
还有其他方法将两个集合连接起来，并且仅保留重复项，或者永远不保留重复项，请查看此页面底部的集合方法完整列表
"""
s2 = {1, 5, 69}
print(s1.union(s2))

"""
add() 向集合添加元素。 
clear() 删除集合中的所有元素。 
copy() 返回集合的副本。 
difference() 返回包含两个或更多集合之间差异的集合。 
difference_update() 删除此集合中也包含在另一个指定集合中的项目。 
discard() 删除指定项目。 
intersection() 返回为两个其他集合的交集的集合。 
intersection_update() 删除此集合中不存在于其他指定集合中的项目。 
isdisjoint() 返回两个集合是否有交集。 
issubset() 返回另一个集合是否包含此集合。 
issuperset() 返回此集合是否包含另一个集合。 
pop() 从集合中删除一个元素。 
remove() 删除指定元素。 
symmetric_difference() 返回具有两组集合的对称差集的集合。 
symmetric_difference_update() 插入此集合和另一个集合的对称差集。 
union() 返回包含集合并集的集合。 
update() 用此集合和其他集合的并集来更新集合。 
"""
