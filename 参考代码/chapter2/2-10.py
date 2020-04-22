import math
x1 = 3.12                     		#样本1数据.
x2 = 3.36                     		#样本2数据.
x3 = 3.08                     		#样本3数据.
x_ = (x1 + x2 + x3) / 3       		#计算样本平均值.
#计算样本总体标准偏差.
s = math.sqrt((math.pow(x1-x_,2) + math.pow(x2-x_,2) + math.pow(x3-x_,2))/3)
print("x_ =",x_)                	     #输出样本平均值.
print("s =",s)                        #输出样本总体标准偏差.
