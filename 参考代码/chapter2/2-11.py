print("Are you happy?")                	#普通字符串，本质是Unicode字符串.
print(u"I am really\u0020pleased.")  	#Unicode字符串.
print(r"d:\friends.txt")              	#非转义字符串的原始字符串.
print(b"rejoice")   			       	#bytes字节串.
print(bytes("中国","GBK"))                    	#编码成字节串，采用GBK编码格式.
print(str(b'\xd6\xd0\xb9\xfa',"GBK"))     		#解码为Unicode编码格式.
print(bytes("中国","UTF-8"))                  	#编码成字节串，采用UTF-8编码格式.
print(str(b'\xe4\xb8\xad\xe5\x9b\xbd',"UTF-8")) 	#解码为Unicode编码格式.
