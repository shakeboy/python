import numpy as np
A = np.mat("3 4;5 6")       				#创建矩阵.
print(A)
print(A.T)                       					#通过转置创建矩阵.
print(A.I)                       					#通过逆阵创建矩阵.
print(np.mat(np.arange(9).reshape(3,3)))     		#通过数组创建矩阵.
