import os, os.path

a = os.getcwd()
b = [f for f in os.listdir(a )]

print("当前路径：",a)
print("当前路径下文件：",b)