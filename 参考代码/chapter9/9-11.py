with open("Shakespeare.txt","r") as fp:
  data = fp.readline()
  print(data.strip())
  print('输出一行后的文件指针在:',fp.tell())    #查看指针位置
  fp.seek(0)    							 #将文件指针重新定位在开始位置.
  print('用seek()将文件指针放回开始处:',fp.tell())
  print('再次输出:',fp.readline())
