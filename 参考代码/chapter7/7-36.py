import numpy as np
from scipy import linalg
mat = np.array([[5,6],[7,8]])
print("方阵:",mat)
print("方阵的行列式:%6.2f."%linalg.det(mat))
print("方阵的逆矩阵:",linalg.inv(mat))
