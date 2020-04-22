#定义类.
class Book:
  def __init__(self,n,p):
    self.name = n
    self.price = p
#创建对象.
book1 = Book("堂·吉诃德",32)
print("书名:",book1.name,"价格:",book1.price)
book1.author = '塞万提斯'                                  #添加对象的实例成员.
print("书名:",book1.name,"作者:",book1.author,"价格:",book1.price)
