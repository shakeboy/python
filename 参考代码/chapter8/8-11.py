import re
str = input("请输入汉字: ")
reg = "^[\u4e00-\u9fa5]{0,}$"
pattern = re.compile(reg)
res = pattern.match(str)
if res:
  print("您输入的字符串全为汉字！")
else:
  print("您输入的字符串不全为汉字！")
