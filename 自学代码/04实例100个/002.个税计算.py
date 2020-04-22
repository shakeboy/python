# 1.https://www.cnblogs.com/LifeIsHardIUsePyhon/p/9058244.html
# 2.
import sys

for i in sys.argv:
    print(i)


def calculator():
    try:
        # a = int(sys.argv[1])
        a = int(input())
        salary = a - 3500
        if salary > 80000:
            cal_salary = salary * 0.45 - 13504
        elif salary > 55000:
            cal_salary = salary * 0.35 - 5505
        elif salary > 35000:
            cal_salary = salary * 0.3 - 2755
        elif salary > 9000:
            cal_salary = salary * 0.25 - 1005
        elif salary > 4500:
            cal_salary = salary * 0.2 - 555
        elif salary > 1500:
            cal_salary = salary * 0.1 - 105
        else:
            cal_salary = salary * 0.03
        print("{:.2f}".format(cal_salary))
    except:
        print("Parameter Error")


calculator()
