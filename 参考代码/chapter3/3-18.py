i = 1; n = 10; sum = 0
while i <= n:
  if i % 2 == 1:           		#i为奇数，跳过.
    i = i + 1
    continue               		#使用continue跳出本次循环.
  sum = sum + i
  i = i + 1
print("sum =",sum)
