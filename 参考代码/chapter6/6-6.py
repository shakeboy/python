#定义类.
class A(object):
  def function_p(self):            			          #定义公有方法.
    print("在公有方法中调用:",self.__function())  	     #调用私有方法.
    return "公有方法 'function_p'"
  def __function(self):            			          #定义私有方法.
    return "私有方法 '__function'"
  @classmethod
  def function_c(cls):            			          #定义类方法.
    return "类方法 'function_c'"
  @staticmethod
  def function_s():             			               #定义静态方法.
    return "静态方法 'function_s'"
#创建对象.
a1 = A()
print("对象调用: " + a1.function_p())
print("对象调用: " + a1.function_c())
print("对象调用: " + a1.function_s())
print("类名调用: " + A.function_p(a1))                 #传递对象a1作为参数.
print("类名调用: " + A.function_c())
print("类名调用: " + A.function_s())
