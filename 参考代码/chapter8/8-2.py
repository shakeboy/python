import re
str = "<div>监督学习</div><div>非监督学习</div><div>半监督学习</div>"   	#字符串.
pat1 = re.compile('<div>.*</div>')    	      #生成正则表达式对象.
res1 = pat1.findall(str)  				 #查找匹配字符串.
print("贪婪匹配:",res1)
pat2 = re.compile('<div>.*?</div>')   	      #生成正则表达式对象.
res2 = pat2.findall(str)  				 #查找匹配字符串.
print("非贪婪匹配:",res2)
