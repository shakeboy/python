import re

iden = input("请输入标识符: ")
reg = "[^\d][\u4E00-\u9FA5a-zA-Z0-9_]{0,}$"    	#正则表达式.
pattern = re.compile(reg)
res = pattern.match(iden)
if res:
  print("您输入的标识符合法！")
else:
  print("标识符包含指定范围外的字符，或没有以中、英文字母或下划线开头。请重新输入！")
