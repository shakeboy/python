str_unicode = "工业"      					#Unicode格式.
print("str_unicode:",type(str_unicode),",",str_unicode)
str_utf8 = str_unicode.encode("UTF-8")    	#Unicode格式转换为UTF-8格式.
print("str_UTF8:",type(str_utf8),",",str_utf8)
str_unicode = str_utf8.decode("UTF-8")     	#UTF-8格式转换国Unicode格式.
print("str_unicode:",type(str_unicode),",",str_unicode)
str_gbk = str_unicode.encode("GBK")       	#Unicode格式转换为GBK格式.
print("str_GBK:",type(str_gbk),",",str_gbk)
str_unicode = str_gbk.decode("GBK")       	#GBK格式转换为Unicode格式.
print("str_unicode:",type(str_unicode),",",str_unicode)
