import tensorflow as tf  	#导入tensorflow.
a = tf.constant([[1,2]])   	#定义一个1×2的矩阵a.
b = tf.constant([[2],[4]])  	#定义一个2×1的矩阵b.
c = tf.matmul(a,b)	#矩阵乘法运算.
sess = tf.Session()	#创建会话.
result = sess.run(c)     	#启动会话.
print("result =",result)   	#输出结果.
