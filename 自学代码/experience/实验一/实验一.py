import math
# 3、在集成环境编写程序，导入math数学模块，从键盘输入一个整数，然后调用math中的函数sqrt（）计算该数的平方根，输出结果
import catch as catch

print("Hello python")
print("请输入一个数")
number = input()

# 转换成int
try:
    number = int(number)
except TypeError:
    print("无效操作，请重新输入：")
print("您输入的数据类型是：")
print(type(45))
print("最终结果是：")
print(math.sqrt(number))
# if type(number)
