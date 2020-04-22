import numpy as np, matplotlib.pyplot as plt
n = 512               							#数据个数
x = np.random.normal(0,1,n)                    	#均值为0, 方差为1的随机数.
y = np.random.normal(0,1,n)                   	#均值为0, 方差为1的随机数.
color = np.arctan2(y,x) 						#计算颜色值.
plt.scatter(x,y,s=75,c=color,alpha=0.6)     	#绘制散点图.
plt.xlim((-2.0,2.0))
plt.ylim((-2.0,2.0))
plt.show()
