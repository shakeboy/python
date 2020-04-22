def cube(x):
 	  return x ** 3
print(list(map(cube,[1,2,3,4,5])))                   	       #计算列表中各个元素的立方和.
def add(x,y):
	  return x + y
print(list(map(add,[1,3,5,7,9],[2,4,6,8,10])))        	#两个列表相同位置的元素相加.
a,b = map(int,input("请输入两个数(用空格隔开): ").split())  #接受接收从键盘输入的两个数.
print("a = %d, b = %d."%(a,b))
