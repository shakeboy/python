def delete():
    str1 = input("请输入字符串str1:")
    str2 = input("请输入字符串str2:")
    if str2 in str1:
        str=str1.replace(str2,'')
    print("删除后的字符串为：",str)

if __name__=="__main__":
    delete()