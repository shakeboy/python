#定义递归函数。
def gys(a,b):
  if a > b:
    a,b = b,a
  if b % a == 0:
    return a
  else:
    return gys(a,b % a)

if __name__ == '__main__':
  num1 = int(input("请输入第一个整数: "))
  num2 = int(input("请输入第二个整数: "))
  print(num1,"和",num2,"的最大公约数为",gys(num1,num2))
