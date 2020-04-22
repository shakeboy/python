from datetime import time
print("时间最大值:",time.max)
print("时间最小值:",time.min)
t = time(20,30,50,8888)             		#创建time对象.
print("时间: %d时%d分%d秒%d微秒."%(t.hour,t.minute,t.second,t.microsecond))
