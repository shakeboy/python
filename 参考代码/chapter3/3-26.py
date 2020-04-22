import random

key = random.randint(1,100)       #生成一个1～100之间的随机整数.
print('------猜数字游戏开始！-----')
count = 0                      #用户猜数的次数.
x = int(input('请输入数字: '))  #用户猜的数字.
while True:
  count = count + 1                 # 用户每猜数1次，count增1.
  if x > key:                   #猜的数大于生成数.
    print('您猜的数字大了！')
  elif x < key:                 #猜的数小于生成数.
    print('您猜的数字小了！')
  else:                        #猜的数等于生成数.
    print('恭喜您，猜对了！')
    break
  if count >= 5:                #超过游戏规定的5次猜数次数.
    print('很遗憾，您没猜中！生成数字是: %d.'%key)
    break
  x = int(input('请输入数字: '))
print('----游戏结束，再见！^_^----')
from math import fabs,sqrt 