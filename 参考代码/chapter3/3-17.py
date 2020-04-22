n1 = 1              			#第1项.
n2 = 1              			#第2项.
count = 2
print("斐波那契数列前10项为:",end=" ")
print(n1,n2,end=" ") 		     #输出前2项.
while True:
  if count >= 10:    			#已经输出前10项，跳出循环.
    break
  nth = n1 + n2     			#计算下一项.
  print(nth,end=" ")  		     #输出第count项.
  n1 = n2
  n2 = nth
  count += 1
