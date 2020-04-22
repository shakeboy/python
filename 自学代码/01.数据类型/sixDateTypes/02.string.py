"""
字符串字面量
python 中的字符串字面量由单引号或双引号括起。
'hello' 等同于 "hello"。
您可以使用 print() 函数显示字符串字面量：

"""
# 打印字符串
print("hello python")
# print函数的官方文档
"""
  print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
  Prints the values to a stream, or to sys.stdout by default.
  Optional keyword arguments:
  file:  a file-like object (stream); defaults to the current sys.stdout.
  sep:   string inserted between values, default a space.
  end:   string appended after the last value, default a newline.
  flush: whether to forcibly flush the stream.
  forcibly:强制的
  """
print("i", "love", "studying", sep='###', end='\n')
# 字符串赋值
a = "Hello"
# 您可以使用三个引号将多行字符串赋值给变量：
print(a)
a = """Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code."""
print(a, end="\n\n")
# 三个单引号赋值字符串变量
a = '''Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code.'''
print(a, end="\n\n")
# 字符串是数组可以索引
"""
字符串是数组
像许多其他流行的编程语言一样，Python 中的字符串是表示 unicode 字符的字节数组。
但是，Python 没有字符数据类型，单个字符就是长度为 1 的字符串。
方括号可用于访问字符串的元素。
"""
a = "Hello World"
print(a[2])
print(a[-1])
print(a[-5:-1])
'''不包括最后一位，包括前面第一位'''
# 字符串可以剪裁
"""
裁切
您可以使用裁切语法返回一定范围的字符。
指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。
"""
print(a[1:6])
# 获取字符串长度
print(len(a))
# 删除q前后空白字符串
print(" ddd  ddd ddd ".strip())
"""
Return a copy of the string with leading and trailing whitespace remove.

If chars is given and not None, remove characters in chars instead.
"""
# upper()返回字符串
print(a.upper())
# replace()
print(a.replace("o", "$$$"))
# lower()
print(a.lower())
# spilt()分隔符
print(a.split(" "))

# 检查字符串
# 如需检查字符串中是否存在特定短语或字符，我们可以使用 in 或 not in 关键字。
print("a:",a)
if "Hello" in a:
    print("Hello在里面！")
else:
    print("Hello不在里面")
if "hello" in a:
    print("hello在里面！")
else:
    print("hello不在里面")

# 字符串连接
# 如需串联或组合两个字符串，您可以使用 + 运算符。
a = "SHIyiZhaO"
b = "like"
c = "studying"
print(a+" "+b+" "+c)
# 字符串格式化
"""
但是我们可以使用 format() 方法组合字符串和数字！
format() 方法接受传递的参数，格式化它们，并将它们放在占位符 {} 所在的字符串中：
"""
c = "hello world"
d = "fighting"
e = "move"
saying = "开始对世界说{2},我们都会{1},准备{0}"
print(saying.format(e, d, c))
