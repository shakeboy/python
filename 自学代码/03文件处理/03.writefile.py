"""
写入已有文件
如需写入已有的文件，必须向 open() 函数添加参数：

"a" - 追加 - 会追加到文件的末尾
"w" - 写入 - 会覆盖任何已有的内容
"""
f = open("03test", "a", encoding="UTF-8")
str = "我是追加的内容"
f.write(str)
# print(f.read())  # 不能直接读取
f.close()
f = open("03test", "r", encoding="UTF-8")
print(f.read())
f.close()

# 解决乱码问题
# https://blog.csdn.net/joyfixing/article/details/79971667
