# Python 日期
# Python 中的日期不是其自身的数据类型，但是我们可以导入名为 datetime 的模块，把日期视作日期对象进行处理。
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.strftime("%A"))
"""
strftime() 方法
datetime 对象拥有把日期对象格式化为可读字符串的方法。
该方法称为 strftime()，并使用一个 format 参数来指定返回字符串的格式
"""
# 显示月份
print(x.strftime("% B"))
"""
%a Weekday，短版本 Wed 试一试 
%A Weekday，完整版本 Wednesday 试一试 
%w Weekday，数字 0-6，0 为周日 3 试一试 
%d 日，数字 01-31 31 试一试 
%b 月名称，短版本 Dec 试一试 
%B 月名称，完整版本 December 试一试 
%m 月，数字01-12 12 试一试 
%y 年，短版本，无世纪 18 试一试 
%Y 年，完整版本 2018 试一试 
%H 小时，00-23 17 试一试 
%I 小时，00-12 05 试一试 
%p AM/PM PM 试一试 
%M 分，00-59 41 试一试 
%S 秒，00-59 08 试一试 
%f 微妙，000000-999999 548513 试一试 
%z UTC 偏移 +0100 试一试 
%Z 时区 CST 试一试 
%j 天数，001-366 365 试一试 
%U 周数，每周的第一天是周日，00-53 52 试一试 
%W 周数，每周的第一天是周一，00-53 52 试一试 
%c 日期和时间的本地版本 Mon Dec 31 17:41:00 2018 试一试 
%x 日期的本地版本 12/31/18 试一试 
%X 时间的本地版本 17:41:00 试一试 
%% A % character % 试一试 
"""