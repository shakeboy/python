def norecur():
    age=10
    for i in range(2,6):
        age+=2
    print("第5个人岁数是：",age)
def recur(i):
    if i==1:
        return 10
    else:
        return recur(i-1)+2
if __name__=="__main__":
    print("非递归：")
    norecur()
    age=recur(5)
    print("递归：")
    print("第5个人岁数是：", age)