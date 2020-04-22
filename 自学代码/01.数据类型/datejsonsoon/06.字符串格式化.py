"""
字符串 format()
format() 方法允许您格式化字符串的选定部分。
有时文本的一部分是你无法控制的，也许它们来自数据库或用户输入？
要控制此类值，请在文本中添加占位符（花括号 {}），然后通过 format() 方法运行值：

"""
quantity = 3
itemno = 567
price = 52
# 格式字符串===》占位符
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""命名索引
您还可以通过在花括号 {carname} 中输入名称来使用命名索引，但是在传递参数值 txt.format(carname = "Ford") 时，必须使用名称：
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Porsche", model="911"))
