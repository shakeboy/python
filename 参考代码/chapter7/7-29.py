import numpy as np
A = np.mat('1, 2; 3, 4')
print(A * 2)                           			#矩阵和数相乘.
B = np.mat('5, 6; 7, 8')
print(A + B)                         		     #两个矩阵相加.
print(A.dot(B))                       		      #两个矩阵点积.
print(np.matmul(A,B))                		      #两个矩阵相乘.
print(np.inner(A,B))                  		      #两个矩阵内积.
print(np.linalg.inv(A))                 	      #逆矩阵.
print(np.linalg.det(A))                 	      #求矩阵的行列式.
