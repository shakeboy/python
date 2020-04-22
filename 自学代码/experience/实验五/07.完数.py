def isWs(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    else:
        return False
if __name__=="__main__":
    n = int(input("请输入一个整数："))
    flag=isWs(n)
    if flag==True:
        print("输入数据是完数")
    if flag==False:
        print("输入数据不是完数")
