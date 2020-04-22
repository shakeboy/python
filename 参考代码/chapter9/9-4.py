str = input("请输入内容：")
with open("Shakespeare.txt","a") as fp:   	#以追加模式打开一个文件，返回文件对象fp.
  fp.write("\n")   						#在文件末尾写入回车符.
  num = fp.write(str)   					#向文件中添加新的字符串.
  print("向文件中追加字符 %d 个！"%(num))
