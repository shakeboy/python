#定义排序函数.
def binary_search(key,list):
  low = 0
  high = len(list) - 1
  while (low <= high):
    middle = int((low + high) / 2)
    if list[middle] > key:    		#在列表的前半部分.
      high = middle - 1
    elif list[middle] < key:  		#在列表的后半部分.
      low = middle + 1
    else:
      return middle        			#关键字对应元素的位置.
  return -1                			#查找失败.

if __name__ == '__main__':
  list = [2,6,13,25,28,37,41,58,69]
  key = int(input("请输入要查找的关键字: "))
  location = binary_search(key,list)
  if location != -1:
    print("要查找的关键字 %d 索引号为 %d." %(key,location))
  else:
    print("关键字 %d 查找失败！"%key)
