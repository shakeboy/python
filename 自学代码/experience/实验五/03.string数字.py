def func(str):
    count_num=0
    count_alp=0
    count_oth=0
    for i in str:
        if i .isdigit():
            count_num+=1
        elif i.isalpha():
            count_alp +=1
        else:
            count_oth+=1
    print("数字个数为：",count_num)
    print("字母个数为：",count_alp)
    print("其他字符个数为：",count_oth)

if __name__=="__main__":
    str=str(input("请输入一个字符串："))
    func(str)