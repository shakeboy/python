# sum = lambda x, y: x + y                      	#定义匿名函数.
# print(sum(3, 4))
# func = lambda a, b=3,c=2: b**2-4*a*c     	#默认值参数.
# print(func(1))
# print(func(1,4,3))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(map(lambda x, y: x + y , list1, list2)))	#使用匿名函数对列表元素运算.
