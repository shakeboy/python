class People:
  #定义构造方法.
  def __init__(self,n,a):
    self.name = n
  #定义公有方法.
  def speak(self):
    print("%s说: 我%d岁." % (self.name,self.age))
#定义Speaker类.
class Speaker():
  #定义构造方法.
  def __init__(self,n,t):
    self.name = n
    self.topic = t
  #定义公有方法.
  def speak(self):
    print("我叫%s，是一个科学家，今天演讲的主题是%s." % (self.name,self.topic))
#定义类Scientist，同时继承类People和类Speaker.
class Scientist(Speaker,People):
  #定义构造方法.
  def __init__(self,n,a,t):
    #调用2个父类的构造方法.
    People.__init__(self,n,a)
    Speaker.__init__(self,n,t)
if __name__ == '__main__':
  #创建Scientist类的对象，传入参数.
  Hawkin = Scientist("霍金",50,"《时间简史》")
  Hawkin.speak()               	#调用继承时排在前面的Speaker类的speak()方法.
