def Fibonacci(n):
    if n <=0:
        return 0
    elif n==1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)
def fun2():
    sum=0
    for i in range(1,11):
        #print(Fibonacci(i))
        sum+=Fibonacci(i)
    return sum

if __name__=="__main__":
    i=int(input("请输入你想得到的项数："))
    b=Fibonacci(i)
    print("第%d项为%d"%(i,b))
    sum=fun2()
    print("10项和为：",sum)