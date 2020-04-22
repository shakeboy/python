list1 = [3,6,1,9,5,8,7,4]
key = int(input("请输入要查找的关键字: "))  #从键盘要查找的关键字.
num = -1
for i in range(len(list1)):
  if list1[i] == key:                 	  #关键字查找成功，则修改标志，跳出循环.
    num = i
    break
if num != -1:
  print("要查找的关键字 %d 索引号为 %d."%(key,num))
else:
  print("关键字 %d 查找失败！"%key)
