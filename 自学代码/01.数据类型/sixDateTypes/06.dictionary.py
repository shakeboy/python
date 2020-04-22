# 字典是一个无序、可变和有索引的集合。在 Python 中，字典用花括号编写，拥有键和值。
dict0 = {
    "name": "石义钊",
    "age": 21,
    "dream": "protect whom i love"
}
print(dict0)
# 访问
print(dict0["name"])
print(dict0.get("age"))
# 更改
dict0.update({"school": "湖北大学"})
print(dict0)
dict0["address"] = "世家"
# 遍历
print(dict0)
for i in dict0:
    print(i, ":", dict0[i])
for i in dict0.values():
    print(i)
for i, j in dict0.items():
    print(i, j)

# 检查键是否存在
thisdict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(dict0))

# 删除项目
dict0.pop("address")
print(dict0)
# popitem() 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目）：
dict.popitem(dict0)
print(dict0)
del dict0["name"]
print(dict0)
"""
复制字典
您不能通过键入 dict2 = dict1 来复制字典，因为：dict2 只是对 dict1 的引用，而 dict1 中的更改也将自动在 dict2 中进行。
有一些方法可以进行复制，一种方法是使用内建的字典方法 copy()。
"""
thisdict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
mydict = thisdict.copy()
print(mydict)
# 制作副本的另一种方法是使用内建方法 dict()。

# 字典嵌套
myfamily = {
    "child1": {
        "name": "Phoebe Adele",
        "year": 2002
    },
    "child2": {
        "name": "Jennifer Katharine",
        "year": 1996
    },
    "child3": {
        "name": "Rory John",
        "year": 1999
    }
}
"""
clear() 删除字典中的所有元素 
copy() 返回字典的副本 
fromkeys() 返回拥有指定键和值的字典 
get() 返回指定键的值 
items() 返回包含每个键值对的元组的列表 
keys() 返回包含字典键的列表 
pop() 删除拥有指定键的元素 
popitem() 删除最后插入的键值对 
setdefault() 返回指定键的值。如果该键不存在，则插入具有指定值的键。 
update() 使用指定的键值对字典进行更新 
values() 返回字典中所有值的列表 
"""
