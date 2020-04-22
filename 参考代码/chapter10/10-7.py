import unittest
#定义测试类.
class TestCaseOfArea(unittest.TestCase):
  #定义测试方法.测试方法必须以test开头.
  def test_area(self):
    area = getArea(3,4)
    #断言方法用来核实得到的结果是否与期望的结果一致.
    self.assertEqual(area,12,msg="测试未通过！")
#定义求矩形面积函数.
def getArea(x,y):
  area = x * y
  return area
#执行测试.
if __name__ == '__main__':
  unittest.main()
