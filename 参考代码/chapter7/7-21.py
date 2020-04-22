import zlib
str = b'What is your name? What is your name? What is your name?'
print("压缩前: %s,字符个数%d."%(str,len(str)))
str_com = zlib.compress(str)            		     #压缩字符串.
print("压缩后: %s, 字符个数%d."%(str_com,len(str_com)))
str_dec = zlib.decompress(str_com)      		#解压字符串.
print("解压后: %s, 字符个数%d."%(str_dec,len(str_dec)))
