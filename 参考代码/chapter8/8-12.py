import re
ipAdd = "202.114.144.191"
reg = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
pattern = re.compile(reg)
res = pattern.match(ipAdd)
if res:
  print("IP地址格式正确！")
else:
  print("IP地址格式不正确！")
