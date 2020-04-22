import re
real = input("请输入带2位小数的实数: ")
reg = "^[0-9]+(.[0-9]{2})?$"
pattern = re.compile(reg)
res = pattern.match(real)
if res:
  print("您输入的数字合法！")
else:
  print("您输入的数字不合法！")
