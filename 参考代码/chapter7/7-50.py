import pandas as pd
import numpy as np
import os

data = pd.read_csv(os.getcwd()+"\\resource\\000001_stock02.csv")
print("1.股票最高价高于9.00元的天数:",(data.loc[(data['high']>=9.00),
['date']].count()).iloc[0])
print("2.股票收盘价分组:",np.where(data['close']>=9.00,'高','低'))
print("3.股票数据的描述性统计:")
print(data.describe())
print("4.股票数据的相关性分析:")
print(data.corr())
