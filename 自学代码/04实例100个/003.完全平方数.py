# 1.https://www.cnblogs.com/yangfeilong/p/9662925.html
# 2.https://blog.csdn.net/scujcc_zls/article/details/76972952
import math


# 1.返回某一个范围的完全平方数
def completeNumber(n):
    try:
        n = int(n)
        for i in range(n):
            for j in range(int(math.sqrt(n))):
                if j ** 2 == i:
                    print(i)
    except:
        print("输入不是数字,请重新输入")


if __name__ == '__main__':
    print("请输入最大的数，让我告诉你所有小于他的正完全平方数")
    a = input()
    completeNumber(a)