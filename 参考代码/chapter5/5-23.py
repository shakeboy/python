import random

#定义抽奖函数.
def cjhs(jxfb):
  zpds = random.randint(1,100)              	      #随机生成[1, 100]之间的整数.
  #根据zpds所在范围返回抽奖类型.
  for jxjg,kdfw in jxfb.items():
    if kdfw[0] <= zpds and  zpds <= kdfw[1]:
      return jxjg

if __name__ == '__main__':
  #各奖项分布比例.
  jxfb = {'特等奖':(1,3),'一等奖':(4,10),'二等奖':(11,30),'三等奖':(31,100)}
  #各奖项奖金.
  jxjj = {'特等奖':10000,'一等奖':5000,'二等奖':1000,'三等奖':300}
  zjqk = dict()                                  	#中奖情况，字典类型.
  #1轮抽奖的次数.
  for i in range(30):
    bczk = cjhs(jxfb)
    zjqk[bczk] = zjqk.get(bczk,0) + 1
  zjj = 0                                           	#总奖金.
  #根据奖项类型和奖项奖金计算所得奖金情况.
  for key,value in zjqk.items():
    if key == "特等奖": zjj = zjj + value * jxjj[key]
    if key == "一等奖": zjj = zjj + value * jxjj[key]
    if key == "二等奖": zjj = zjj + value * jxjj[key]
    if key == "三等奖": zjj = zjj + value * jxjj[key]
  print("本轮游戏中奖情况:",zjqk)
  print("本轮游戏共获得总奖金 =",zjj)
