i = 1
sum = 1
n = 1
while 1 / n >= 0.00001:
  sum = sum + 1 / n                                           # 计算阶乘的和.
  i = i + 1
  n = n * i                                                     # 计算阶乘.
print("sum =", sum)
