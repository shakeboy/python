list1 = [8,3,1,5,2]             		     #创建列表.
N = list1.__len__()              			#列表中元素个数.
print('排序之前:',end = ' ')
for i in range(N):
  print(list1[i],end = ' ')
print()
#排序.
for i in range(N - 1):
  min = i
  for j in range(i + 1,N):
    if list1[min] > list1[j]: min = j
  list1[i],list1[min] = list1[min],list1[i]
print('排序之后:',end = ' ')
for i in range(N):
  print(list1[i],end = ' ')
