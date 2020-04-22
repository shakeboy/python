import numpy as np
a = np.arange(8)
print(a.reshape(2,4))                   		#改变数组形状.
print(np.transpose(a.reshape(2,4)))       		#数组转置.
print(a.reshape(2,4).ravel())              		#数组展开.
for element in a.flat:                	#数组元素迭代.
      print(element, end=" ")
