"""
已知list=[1,2,3,4,5,6,7,8,9,10]，使用Python内置函数完成如下功能：
(1)将列表list中的元素按奇数和偶数进行过滤，将结果分别存储到2个新列表(list1和list2)中。
(2)将list1中的元素作为10位数和list2中对应位置的元素相加，将结果保存到列表list3中。
"""


def add(li1, li2, li3):
    for i in range(len(li1)):
           li3.append(10 * li1[i] + li2[i])


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li1 = []  # 奇数
li2 = []  # 偶数
li3 = []
for num in li:
    if num % 2 == 0:
        li2.append(num)
    else:
        li1.append(num)
print(li1)
print(li2)
add(li1, li2, li3)
print(li3)
