#定义People类.
class People:
  #定义构造方法.
  def __init__(self,n,a):
    self.name = n
    self.age = a
  #定义公有方法.
  def speak(self):
    print("我是%s，今年%d岁." % (self.name,self.age))
#定义Student类，继承类People.
class Student(People):
  def __init__(self,n,a,g):
    People.__init__(self,n,a)                 #调用父类的构造方法.
    self.grade = g
  #重写父类的方法.
  def speak(self):
    print("我是%s，今年%d岁，读%d年级." % (self.name,self.age,self.grade))
if __name__ == '__main__':
  #创建Student类的对象.
  s = Student('孔融',10,4)
  s.speak()       		                         #调用Student类中的speak()方法.
  super(Student,s).speak()                    #调用父类People的speak()方法.
