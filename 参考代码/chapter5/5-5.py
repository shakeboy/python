#定义函数.
def changeList(myList):
  myList.append(4)                     	#在列表myList末尾增加一个新元素.
list1 = [1,2,3]                            #定义列表list1.
print("调用前list1:",list1)
changeList(list1)                      	#调用函数changeList().
print("调用后list1:",list1)
