for x in range(51): 			#x为公鸡只数，100元最多买50只.
  for y in range(34):       	#y为母鸡只数，100元最多买33只.
    z = 100 - x - y			#z为小鸡只数.
    if 2 * x + 3 * y + 0.5 * z == 100:
      print("公鸡 %d 只，母鸡 %d 只，小鸡 %d 只."%(x,y,z))
