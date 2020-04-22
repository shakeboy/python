import numpy as np
a = np.array([[1,2],[3,4]])
print(a * 2)                           			#数组与数相乘.
b = np.array([[5,6],[7,8]])
print(a + b)                          			#两个数组相加.
print(np.dot(a,b))                    		     #两个数组的内积.
print(np.matmul(a,b))                		     #两个数组的矩阵乘法.
print(np.vdot(a,b))                   		     #两个数组的点积.
print(np.inner(a,b))                   		     #两个数组的向量内积.
print(np.linalg.det(a))                 	     #求矩阵行列式.
print(np.linalg.inv(a))

np.linalg.inv(a)                 	     #求逆阵.
