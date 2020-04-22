from datetime import datetime
dt = datetime.now()
print("当前日期:",dt.date())
print("当前时间:",dt.time())
print("当前年份: %d,当前月份: %d,当前日期: %d."%(dt.year,dt.month,dt.day))
print("时间:",datetime(2018,9,16,12,20,36))   	#创建日期时间对象.
