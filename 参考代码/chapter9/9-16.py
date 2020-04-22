import marshal
#创建数据.
data1 = ['def',34,87]  					      #数据.
data2 = {1:'优秀',2:'良好',3:'合格',4:'不合格'}    #数据.
data3 = (5,6,7)                                       #数据.
with open("marshal_file.dat",'wb') as output_file:
  marshal.dump(data1,output_file)  		#数据序列化.
  marshal.dump(data2,output_file)  		#数据序列化.
  marshal.dump(data3,output_file)  		#数据序列化.
  print("写入数据成功！")
