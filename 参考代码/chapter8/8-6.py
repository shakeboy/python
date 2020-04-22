import re
str = "of the people, for the people，by the people."   	#字符串.
res = re.finditer("\w+ \w+ (people)", str)  				#匹配字符串.
for match in res:
  print(match.group())
