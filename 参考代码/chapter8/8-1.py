import re
str = '今天是2019-05-01, 劳动节!'  			#字符串.
reg = '\d{2,4}-\d{1,2}-\d{1,2}'     		#正则表达式.
res = re.findall(reg,str)     			     #提取匹配字符串.
print("日期:",res)
