import re
str = "0086-010-88668866"    	            #中国国际长途电话.
mat = re.match(r"(?P<nation>\d{4,})-(?P<zone>\d{3,4})-(?P<number>\d{7,8})",str,
 		re.M | re.I)
if mat:
  print("mat.group(0):",mat.group(0))
  print("mat.group(1):",mat.group(1))
  print("mat.group(2):",mat.group(2))
  print("mat.group(3):",mat.group(3))
  print("mat.group(1,2,3):",mat.group(1,2,3))
  print("mat.groups():",mat.groups())
  print("mat.groupdict():",mat.groupdict())
else:
  print("match匹配不成功！")
