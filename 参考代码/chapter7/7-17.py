import os
print("(路径,文件):",os.path.split(r"d:\pythonProjects\p1\test1.py"))
print("目录存在?:",os.path.exists(r"d:\pythonProjects\p1"))
print("文件存在?:",os.path.isfile(r"d:\pythonProjects\p1\test1.py"))
print("文件大小:",os.path.getsize(r"d:\pythonProjects\p1\test1.py"))
