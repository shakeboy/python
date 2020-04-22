#定义外函数.
def outerFunc(x):
  #定义内函数.
  def innerFunc(y):
    return x * y
  return innerFunc                          #调用内函数.
print("方法一调用结果:",outerFunc(3)(4))  #调用时，同时传递外函数参数和内函数参数.
a = outerFunc(3)                            #调用外函数，传递外函数参数.
print("方法二调用结果:",a(4))               #间接调用内函数，传递内函数参数.
