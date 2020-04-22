#定义带参数的装饰器.
def DECO(args):
  #定义内部装饰器.
  def deco(func):
    #定义内部函数.
    def call_func(x,y):
      print("%d %s %d = "%(x,args,y),end='')
      return func(x,y)
    return call_func
  return deco
#传递装饰器参数.
@DECO('&')
def andFunc(x,y):                                            #按位'与'运算.
  return x & y
#传递装饰器参数.
@DECO('|')
def orFunc(x,y):                                             #按位'或'运算.
  return x | y
if __name__ == "__main__":
  print(andFunc(5,6))
  print(orFunc(5,6))
