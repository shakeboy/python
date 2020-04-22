import marshal
with open('marshal_file.dat','rb') as marshal_file:	#从文件中读取序列化的数据.
  data1 = marshal.load(marshal_file)    			#数据反序列化.
  data2 = marshal.load(marshal_file)    			#数据反序列化.
  data3 = marshal.load(marshal_file)    			#数据反序列化.
  print(data1)
  print(data2)
  print(data3)
