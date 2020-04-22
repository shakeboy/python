list1 = [2,1,3,4,7,11,18,29]  		#卢卡斯数.
try:
  print(list1[7])
except IndexError as e:
  print("列表索引超出范围！")
