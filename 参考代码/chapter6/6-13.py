#定义类Animal.
class Animal():
  #定义方法.
  def getInfo(self):
    return "I am an animal."
#定义类Lion，继承类Animal.
class Lion(Animal):
  #重写父类Animal的方法getInfo().
  def getInfo(self):
    return "I am a lion."
#定义类Tiger，继承类Animal.
class Tiger(Animal):
  #重写父类Animal的方法getInfo().
  def getInfo(self):
    return "I am a tiger."
#定义类Leopard，继承类Animal.
class Leopard(Animal):
  #重写父类Animal的方法getInfo().
  def getInfo(self):
    return "I am a leopard."
if __name__ == '__main__':
  #创建各个类的对象列表objectList.
  objectList = [item() for item in (Animal,Lion,Tiger,Leopard)]
  #不同对象调用同一方法getInfo().
  for object in objectList:
    print(object.getInfo())
