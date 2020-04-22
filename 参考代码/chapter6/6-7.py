#定义类.
class Circle:
  def set(self,radius):
    if radius >  0:
      self.__radius  =  radius
      print("圆的面积为: {0}.".format(3.14 * self.__radius ** 2))
    else:
      print("半径 %f 不在规定范围内(>=0)，请重新设置!"% radius)
  def get(self):
    return self.__radius                                          #私有实例成员.
#创建对象.
c = Circle()
c.set(2.5)
c.set(-2.5)
