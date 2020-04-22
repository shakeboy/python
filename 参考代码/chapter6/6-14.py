import abc
#定义抽象类.
class People(metaclass=abc.ABCMeta):
  #定义抽象方法.
  @abc.abstractmethod
  def working(self):
    pass
#定义抽象类People的派生类.
class Chinese(People):
  #实现抽象类的抽象方法working().
  def working(self):
    print("中国人都在勤奋地工作…")
#创建Chinese类的对象.
c1 = Chinese()
c1.working()
