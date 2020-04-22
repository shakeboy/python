#定义类.
class Student:
  chinese = 142                         	#定义类成员.
  maths = 1                             	#定义类成员.
  english = 141                          	#定义类成员.
  #定义构造方法.
  def __init__(self,name):
    self.name = name                    	#定义实例成员self.name，name为局部变量.
#创建对象.
s1 = Student("马允")
print(s1.name + "的语文成绩: " + str(Student.chinese))
print(s1.name + "的数学成绩: " + str(Student.maths))
print(s1.name + "的英语成绩: " + str(Student.english))
