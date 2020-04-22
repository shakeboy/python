x = int(input("请输入一个整数: "))
y = int(input("请输入一个整数: "))
if x < y:
  x,y = y,x
print("%d, %d"%(x,y))
