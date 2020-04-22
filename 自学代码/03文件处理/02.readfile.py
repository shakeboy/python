"""
只读取文件的一部分
默认情况下，read() 方法返回整个文本，但您也可以指定要返回的字符数：
"""
# 读取前五个字符
f = open("01test", "r", encoding="UTF-8")
print(f.read(5))
# 读取某一行
print(f.readline())

# 过循环遍历文件中的行，您可以逐行读取整个文件：
f = open("02test", "r", encoding="UTF-8")
for i in f:
    print(i)

# 读取完后关闭文件
f.close()