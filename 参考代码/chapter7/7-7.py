import random
list1 = [1,2,3,4,5,6,7,8]
for x in range(1,4):
  r = random.choice(list1) 		#每次随机获取列表中的一个数.
  print("r =",r)
