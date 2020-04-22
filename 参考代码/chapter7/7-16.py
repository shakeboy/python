import os
print("当前工作路径:",os.getcwd())
print("当前路径的目录和文件列表:",os.listdir())
os.rename("test1.py","test2.py")
print("重命名文件后,当前路径的目录和文件列表:",os.listdir())
os.mkdir("newDir")
print("创建新目录后,当前路径的目录和文件列表:",os.listdir())
os.chdir("newDir")
print("改变当前工作路径后, 当前工作路径:",os.getcwd())
