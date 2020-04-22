import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split

#1.生成数据集.
x,y=datasets.make_regression(n_samples=200,n_features=1,n_targets=1,noise=6)
#生成数据点以散点图显示.
print("1.生成数据的散点图(图15.2左),训练数据和预测数据拟合线(图15.2右).")
plt.scatter(x,y)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('x轴 - x',fontproperties='SimHei',fontsize=18)
plt.ylabel('y轴 - y',fontproperties='SimHei',fontsize=18)
plt.show()
#2.拆分数据集.70%数据用于训练，30数据用于测试.
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=0)
#3.训练模型.
LinearModel = LinearRegression()
LinearModel.fit(train_x,train_y)
fitted_y = LinearModel.predict(train_x)
#图形显示训练数据和预测数据.
plt.plot(train_x,train_y,'bo')
plt.plot(train_x,fitted_y,'r',linewidth = 4.0)
plt.xlabel('x轴 - train_x',fontproperties='SimHei',fontsize=18)
plt.ylabel('y轴 - train_y/fitted_y',fontproperties='SimHei',fontsize=18)
plt.legend(['train_y','fitted_y'],fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
#4.模型评估.
print("2.模型评估值: %.6f."%LinearModel.score(test_x,test_y))
#5.保存模型.
joblib.dump(LinearModel,'TrainModel.m')
#6.使用模型.
LinearModelUse = joblib.load('TrainModel.m')
testx = [[1.6]]
print("3.%f 的预测结果为: %f."%(testx[0][0],LinearModelUse.predict([[1.6]])))
