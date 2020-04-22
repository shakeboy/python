import re
str = "David的QQ电子邮箱:123456@qq.com"
sea = re.search(r"(?P<user>\d+)@(?P<website>\w+)\.(?P<extension>\w+)",str,re.M | re.I)
if sea:
  print("sea.group(0):",sea.group(0))
  print("sea.group(1,2, 3):",sea.group(1,2,3))
  print("sea.groups():",sea.groups())
  print("sea.groupdict():",sea.groupdict())
else:
  print("search匹配不成功！")
