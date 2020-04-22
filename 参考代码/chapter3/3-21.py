for i in range(1,5):                   		#行数为4.
  for j in range(1,5):                 		#列数为4.
    if i == j or i + j == 5:
      print("1",end='  ')               		#输出1.
    else:
      print("0",end='  ')               		#输出0
  print()                              			#换行.
