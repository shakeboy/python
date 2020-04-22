from datetime import date
d = date.today()
print("当前本地日期:",d)
print("日期: %d 年 %d 月 %d 日."%(d.year,d.month,d.day))
print("今天是周 %d."%d.isoweekday())
