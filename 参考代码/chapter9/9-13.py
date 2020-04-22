import pickle
with open("pickle_file.dat","rb") as pickle_file:		#打开二进制文件.
  data1 = pickle.load(pickle_file)    			 		#读二进制数据.
  print("data1:",data1)
  data2 = pickle.load(pickle_file)
  print("data2:",data2)
