import time,threading
#thBoss创线程将调用函数.
def bossFunc(thName):
  print("%s：今晚加班到11:30."%thName)
  event.isSet() or event.set()
  time.sleep(6)
  print("%s：大家一起去吃夜宵 ..."%thName)
  event.isSet() or event.set()
#thEmployee线程将调用函数.
def employeeFunc(thName,i):
  event.wait()
  print("%s %d: 好痛苦 ..."%(thName,i))
  time.sleep(1)
  event.clear()
  event.wait()
  print("%s %d: 太好了！"%(thName,i))
if __name__ == '__main__':
  #创建event对象.
  event = threading.Event()
  #创建线程thBoss.
  thBoss = threading.Thread(target=bossFunc,args=("thBoss",)).start()
  #创建线程thEmployee.
  for i in range(2):
    thEmployee = threading.Thread(target=employeeFunc,args=("thEmployee",
 		i)).start()
