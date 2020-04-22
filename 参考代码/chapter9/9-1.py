file = open("d:/data1.txt","w")    		#打开一个文件用于写入.
print("文件名字:",file.name)
print("访问模式:",file.mode)
print("是否已关闭:",file.closed)
file.close()                                    #关闭文件.
