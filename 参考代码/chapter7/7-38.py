import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]          #创建x轴数据.
y = [3,5,6,9,13,6,32,111]		#计算y轴数据.
plt.xlim((0,10))         		#设置x轴刻度范围.
plt.ylim((0,120))          		#设置y轴刻度范围.
plt.xlabel('x轴',fontproperties='SimHei',fontsize=16)    #设置x轴字体.
plt.ylabel('y轴',fontproperties='SimHei',fontsize=16)    #设置y轴字体.
plt.plot(x,y,'r',lw=2)  	     #(x、y):坐标，'r':红色，lw:线宽.
plt.show()              		#显示图形.
