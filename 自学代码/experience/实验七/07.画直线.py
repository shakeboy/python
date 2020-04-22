import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

#绘制在同一个figure中
plt.figure()
plt.xlabel('X轴')
plt.ylabel('Y轴')
l1, = plt.plot(x,y1,label='y1=2*x+1')#放在handles中l1一定要加，
l2, = plt.plot(x,y2,color='red',linewidth = 2.0,linestyle = '--',label='y2=x^2')

plt.legend(handles=[l1, l2,],labels=['y1=2x+1','y2=x^2'],loc='best')
plt.show()