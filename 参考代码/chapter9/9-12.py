import pickle
list1 = [2,4,5,8]                                             #数据.
tuple1 = ("music","game","sports")                         #数据.
data = [list1,tuple1] 								#数据.
with open("pickle_file.dat","wb") as pickle_file:       #打开二进制文件.
  for i in data:
    pickle.dump(i,pickle_file)     					     #写入数据.
  print("写入数据成功！")
