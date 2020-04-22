import datetime,time
# 获取当前时间
now = datetime.datetime.now()
# 格式化时间字符串
str_time = now.strftime("%Y-%m-%d %A")
year=now.year
month=now.month
day=now.day
print("年份：",year)
print("月份：",month)
print("日：",day)
print(str_time)