class Rectangle(object):
  #定义构造方法.
  def __init__(self,w,h):
    self.w = w
    self.h = h
    print('执行构造方法...')
  #定义求面积方法.
  def getArea(self):
    return self.w * self.h
#定义析构方法.
  def __del__(self):
    print('执行析构方法...')
if __name__ == '__main__':
  rect = Rectangle(3,4)           	      #创建对象，调用构造方法__init__().
  print("面积为:",rect.getArea())
  del rect 		                          #删除对象，调用析构方法__del__().
