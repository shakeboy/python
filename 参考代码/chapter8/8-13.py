import re

pattern = re.compile('[1-9]\d*\.?\d*') 			     #生成正则表达式对象.
str = "本月消费:公积金1028.90元,失业保险费21.60元,房租1250.00元,生活费1868.20元,电话费194.36元,交通费113.52元,其它费用201.30元"		#待匹配字符串.
res = pattern.findall(str)
sum = 0.0
for fee in res:
  sum = sum  + float(fee)
print("您本月的总消费为:%8.2f元."%sum)
