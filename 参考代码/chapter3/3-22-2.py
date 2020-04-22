sum = 1
n = 1
for i in range(1,10000):
  n = n * i                                     #计算阶乘.
  if 1 / n >= 0.00001:
    sum = sum + 1 / n                         #计算阶乘的和.
  else:
    break
print("sum =",sum)
