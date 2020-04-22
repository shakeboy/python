mul = 1; i = 1; sum = 0
while i <= 10:
  mul = mul * i                      		#计算阶乘.
  sum = sum + mul                  		#计算和.
  i = i + 1
else:
  print("循环结束！")                    	#结束循环提示.
print("sum =",sum)
