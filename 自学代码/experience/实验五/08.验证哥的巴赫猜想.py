import math
def isprime(n):  # 判断素数
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
def thonsand(n):  # 生成若干个素数，返回素数list
    a = []
    for i in range(1, n + 1):
        if isprime(i):
            a.append(i)
    return a
def isGDBH(n):
    a = []
    ls = thonsand(n)
    for i in ls:
        for j in ls:
            if i<=j:
                if n == i + j:
                    a.append(str(n)+"="+str(i)+"+"+str(j))
    return a
if __name__=="__main__":
    n = int(input("请输入一个6-100之间的偶数："))
    print(isGDBH(n))