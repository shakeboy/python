#定义装饰器.
def deco(func):
  #定义内函数.
  def modify_text(str):
    return "<strong>" + func(str) + "</strong>"
  return modify_text
#使用装饰器修饰函数.
@deco
def textFunc(str):
  return str
print(textFunc("text"))
