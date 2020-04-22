#定义类.
class Test():
  def __get(self):                                   #读成员的方法.
    return self.__value
  def __set(self,value):                            #写成员的方法.
    self.__value = value
  def __del(self):                                   #删除方法.
    del self.__value
  value = property(__get,__set,__del)            #设置属性为可读、可写和可删除.
#创建类Test的对象.
t = Test()
t.value = 100                                         #写成员.
print("value = %d."%t.value)                       #读成员.
del t.value                                           #删除成员.再次访问，则出错.
print("value = %d."%t.value)
