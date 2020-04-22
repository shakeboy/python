import struct
with open("struct_file.dat","rb") as struct_file:
  binary1= struct_file.read()					     #读出二进制数据.
a,b,c = struct.unpack("5sif",binary1)  		     #反序列化.
print("a:",a.decode("UTF-8"))
print("b:",b)
print("c: %.2f"%c)
