import numpy as np
import pandas as pd

data = [['apple',10],['orange',12],['pear',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print ("数据帧为：\n",df)
num1 = df.iloc[[0]]
print("第一行：\n",num1)
num2=df.loc[:,['Name']]
print("第一列：\n",num2)
detail=df.iat[1,1]   #选取第二行第二列，用于已知行、列位置的选取。
print("第二行第二列：",detail)