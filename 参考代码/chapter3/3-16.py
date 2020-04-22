# sum = 0
# for i in range(0,21,3):  		     #范围0～20，不包括21，步长为3.
#   sum = sum + i       				#计算和.
# print('sum =',sum)     			#输出结果.

sum = 0
for i in range(1,21):   		#范围1～20，不包括21.
  if i % 3 == 0:       		#能被3整除，则余数为0.
    sum = sum + i    			#计算和.
print('sum =',sum)    		     #输出结果.
