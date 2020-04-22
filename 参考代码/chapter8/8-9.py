import re
pattern = re.compile('wr\w+ \w+') 		#生成正则表达式对象.
#匹配字符串.
res = pattern.findall("Frankly,in the opinion of the Joint Chiefs of Staff,this strategy would involve us in the wrong war,at the wrong place,at the wrong time,and with the wrong enemy.")
if res:
  print("匹配结果：",res)
else:
  print("匹配无结果！")
