class Woman():
  def __init__(self, birth):
    self.__birth = birth
  @property                          #设置属性为可读.
  def salary(self):
    return self.__salary
  @salary.setter                    #设置属性为可写.
  def salary(self, salary):
    self.__salary = salary
  @property                          #设置属性为只读.
  def birth(self):
    return self.__birth
#创建对象.
w1 = Woman("1992.06.06")
w1.salary = 10800.00
print("您的出生日期: %s, 薪水: %.2f 元." % (w1.birth, w1.salary))
