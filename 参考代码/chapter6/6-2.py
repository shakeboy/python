#定义类.
class Woman:
  def __init__(self,name,sex,age):
    self.name = name                             #定义公有成员.
    self._sex = sex                              #定义单下划线私有成员.
    self.__age = age                             #定义双下划线私有成员.
  def getAge(self):
    return self.__age
#创建对象.
w = Woman("小芳","Female",18)
print("姓名: %s, 性别: %s, 年龄: %d."%(w.name,w._sex,w.getAge()))
