import re
str = "多少事,从来急;天地转,光阴迫.一万年太久,只争朝夕.—毛泽东"    	#字符串.
strList = re.split('\W+',str)     						     #提取字符串.
print("strList =",strList)
