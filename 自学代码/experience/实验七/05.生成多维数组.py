import numpy as np

data = np.random.randint(1,100,size=[3,4]) #创建一个2行3列的随机数组
print(data)
average=0
average_all=0
sum=0
for i in data:
    sum+=i
average=sum/4
sum=0
for i in average:
    sum+=i
average_all=sum/3
print("平均值为：",average_all)