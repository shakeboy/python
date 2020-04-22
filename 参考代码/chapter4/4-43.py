list1 = [8,3,1,5,2]
N=list1.__len__()
print('排序之前:',end = ' ')
for i in range(N):
  print(list1[i],end = ' ')
print()
#排序.
for i in range(N - 1):
  for j in range(i + 1,N):
    if list1[i] > list1[j]:
      list1[i],list1[j] = list1[j],list1[i]
print('排序之后:',end = ' ')
for i in range(N):
  print(list1[i],end = ' ')
