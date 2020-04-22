import struct
a = "Hello"
b = 35
c = 89.46
binary1 = struct.pack('5sif',a.encode("UTF-8"),b,c)
with open("struct_file.dat","wb") as struct_file:
  struct_file.write(binary1)   					#向文件中写入数据.
print("写入数据成功！")
