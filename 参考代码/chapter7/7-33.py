import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(9).reshape((3,3)),index=['A','B','C'],columns=['one','two','three'])
print(df)                                                   #数据帧.
print(df[1:2])                                             #选取行数据.
print(df[['three','one']])                               #选取列数据.
print(df[df['three'] > 5])                               #数据过滤.
print(df.loc['A','two'])                                 #使用.loc()选取单个数据.
print(df.iloc[1,1])                                      #使用.iloc()选取单个数据.
