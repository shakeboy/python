year = int(input("请输入年份："))
month = int(input("请输入月份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("该年是闰年！")
    if month == 2:
        print("该月有29天")
else:
    print("该年不是闰年！")
    if month == 2:
        print("该月有28天")
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("该月有31天")
if month == 4 or month == 6 or month == 9 or month == 11:
    print("该月有30天")
