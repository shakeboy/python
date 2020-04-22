import re

while True:
  password = input("请输入密码: ")					#输入密码.
  password_again = input("请再次输入密码: ")  		#再次输入密码.
  if password == password_again:
    break
  else:
    print("两次输入的密码不相同。请重新输入！")
reg = "^(?!\d+$)[\dA-Za-z_]{6,20}$"     			#正则表达式.
pattern = re.compile(reg)
res = pattern.match(password)
if res:
  print("您输入的密码合法！")
else:
  print("密码包含指定范围外的字符，或者全为数字，或者字符个数超出范围。请重新输入！")
