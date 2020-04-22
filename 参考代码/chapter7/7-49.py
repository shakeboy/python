import numpy as np,os
import matplotlib.pyplot as plt

#将000001_stock01.csv中的第4列(收盘价)、6列(成交量)数据读到数组c、v中.
close,volume=np.loadtxt(os.getcwd()+"\\resource\\000001_stock01.csv",
delimiter=',',usecols=(3,5),unpack=True)
print("收盘价的算术平均价格:%6.2f 元."%np.mean(close))
print("成交量的算术平均值:%10.2f 手."%np.mean(volume))
#计算收盘价的加权平均价格(时间越靠近现在权重越大).
t = np.arange(len(close))
print("收盘价的加权平均价格:%6.2f 元."%(np.average(close,weights=t)))
#将000001_stock01.csv中的第3列(最高价)、5列(最低价)数据读到数组high、low中.
high,low = np.loadtxt(os.getcwd()+"\\resource\\000001_stock01.csv",delimiter=
',',usecols=(2,4),unpack=True)
print("股票最高价格:%6.2f 元."%np.max(high))
print("股票最低价格:%6.2f 元."%np.min(low))
print("股票最高价格波动范围:%6.2f 元."%np.ptp(high))
print("股票最低价格波动范围:%6.2f 元."%np.ptp(low))
"""----------显示股票000001在2018年7月的收盘价走势图--------------"""
#将000001_stock01.csv中的第1列(日期)数据读到数组date中.
date = np.loadtxt(os.getcwd()+"\\resource\\000001_stock01.csv",dtype=str,delimiter
=',',usecols=(0,),unpack=True)
plt.plot(date,close,'r',lw=2)
plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel('x轴-日期',fontsize=14)
plt.ylabel('y轴-收盘价(元)',fontsize=14)
plt.legend(['收盘价(元)'])
plt.gcf().autofmt_xdate()
plt.show()
