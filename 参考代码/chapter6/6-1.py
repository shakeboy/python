#定义类.
class Car:
  #定义构造方法.
  def __init__(self,name):
    self.name = name
  #定义方法.
  def getName(self):
    return self.name
#创建对象.
c1 = Car("奔驰")
print("这辆汽车的品牌:",c1.getName())
