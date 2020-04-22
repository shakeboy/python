def func(n):
    sum = 0
    if n%2 == 0:
        for i in range(1,n+1):
            sum += 1/2*i
    else:
        for i in range(0,n+1):
            sum += 1/(2*i+1)
    print("结果为：", sum)


if __name__=="__main__":
    n=int(input("请输入一个整数："))
    func(n)