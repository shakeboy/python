a = 3; b = 2; c = 4
if a > b:           			#条件为True，只需要比较a和c.
  if a > c:         			#即：a > b且a > c.
    print("最大的数是：",a)
  else:             			#即：a > b且a <= c.
    print("最大的数是：",c)
else:               			#条件为False，只需要比较b和c.
  if b > c:         			#即：b >= a且b > c.
    print("最大的数是：",b)
  else:             			#即：b >= a且b < c.
    print("最大的数是：",c)
