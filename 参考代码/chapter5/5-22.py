#定义装饰器.
def deco(func):
  #检查func(x,y)中的参数.
  def check_call_func(x,y):
    if x > 0 and y > 0:
      return func(x,y)
    else:
      return "提示: 函数参数 " + str(x)+" 和 "+str(y)+" 必须为正数!"
  return check_call_func

@deco
def rec_area(x,y):                                  #计算长方形面积.
  return x * y

@deco
def rec_perimeter(x,y):                         	#计算长方形周长.
  return 2 * (x + y)

if __name__ == "__main__":
  print(rec_area(-3,4))
  print(rec_perimeter(-3,4))
  print(rec_area(3,4))
  print(rec_perimeter(3,4))
