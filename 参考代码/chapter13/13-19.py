import threading,queue,random

#定义线程类.
class MyThread(threading.Thread):
  #重写构造方法.
  def __init__(self,cpfx_q,i,zjhm,lock):
    super(MyThread,self).__init__()	#调用父类构造函数.
    self.cpfx_q = cpfx_q
    self.i = i
    self.zjhm = zjhm
  #重写run()方法.
  def run(self):
    lock.acquire()
    zjxx = self.cpfx_q.get()   	#中奖信息出队列.
    cphmList = self.cpfx_q.get()   	#可购买的彩票号码列表出队列.
    cphm = random.choice(cphmList)    	#模仿随机购买彩票.
    cphm_num = cphmList.index(cphm)  	#查找购买彩票号码在列表中的位置.
    #比较购买的彩票号码和中奖号码是否相同.
    if cphm == self.zjhm:
      zjxx = "抽奖人 " + str(self.i) + " 号购买的彩票 " + str(cphm) + " 中奖了!恭喜您！"
    #从可购买的彩票号码列表中删除已经购买的彩票号码.
    cphmList.pop(cphm_num)
    self.cpfx_q.put(zjxx)     	#中奖信息入队列.
    self.cpfx_q.put(cphmList)     	#可购买的彩票号码列表入队列.
    lock.release()

if __name__ == '__main__':
  print("-----------------------彩票发行开始...----------------------")
  cpfx_q = queue.Queue()   	#创建彩票发行队列.
  cphmList = list(range(1000,10000))     	#可购买的彩票号码列表: 4位数字.
  random.shuffle(cphmList) 	#将可购买彩票号码列表中彩票号码乱序.
  zjxx = "无人中奖！"  	#中奖信息.
  cpfx_q.put(zjxx)     	#中奖信息入队列.
  cpfx_q.put(cphmList)	#可买的彩票号码列表入队列.
  zjhm = random.randrange(1000,9999)  	#随机生成中奖号码.
  print("本次发行彩票中奖号码:",zjhm)
  lock = threading.Lock()
  #模拟购买彩票，每个线程对应一次购买彩票.
  for i in range(5000):
    MyThread(cpfx_q,i,zjhm,lock).start()
  print("本次彩票发行结果:",cpfx_q.get())
  print("-----------------------彩票发行结束!!!-----------------------")
