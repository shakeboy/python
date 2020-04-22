ygss = float(input("请输入月工时数: "))
if ygss > 180:
  ygz = 80 * ygss + (ygss - 180) * 80 * 0.2
elif ygss >= 120 and ygss <= 180:
  ygz = 80 * ygss
else:
  ygz = 80 * ygss * (1-0.1)
print("您这个月的工资为: %.2f元."%ygz)
