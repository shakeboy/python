import tensorflow as tf
import matplotlib.pyplot as plt
import time

#1. 下载并安装MNIST数据集.
import tensorflow.examples.tutorials.mnist.input_data as inputdata
mnist = inputdata.read_data_sets("MNIST_data/",one_hot=True)

#2. 构建模型
x = tf.placeholder(tf.float32,[None,784])   	#图像数据.
y_real = tf.placeholder("float",[None,10])   	#标签真实值.
#学习参数: 参数矩阵W, 偏置b.
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y_predict = tf.nn.softmax(tf.matmul(x,W) + b)	#标签预测值.
#反向传播结构.
train_cost = -tf.reduce_sum(y_real * tf.log(y_predict))     	#损失函数.
#优化器.
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(train_cost)
#设置模型保存路径.
saver = tf.train.Saver()
model_path = "model/mnist_model.ckpt"
train_epochs = 200    	#训练轮数.
batch_size = 100 	#每轮训练数据量.
#创建字典, 保存训练过程中参数信息.
train_info = {"epoch":[],"train_cost":[],"train_accuracy":[]}
#启动会话.
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer()) #初始化.
  # 3. 训练模型.
  start_time = time.time()
  print("1.训练模型")
  for epoch in range(1,train_epochs + 1):
    batch_xs,batch_ys = mnist.train.next_batch(batch_size) #训练数据.
    opt,cost=sess.run([optimizer,train_cost],feed_dict={x:batch_xs,y_real:batch_ys})
    #计算识别准确率.
    train_cor_pred = tf.equal(tf.argmax(y_predict,1),tf.argmax(y_real,1))
    train_accuracy = tf.reduce_mean(tf.cast(train_cor_pred,tf.float32))
    train_acc = train_accuracy.eval({x:batch_xs,y_real:batch_ys})
    #保存训练信息.
    train_info["epoch"].append(epoch) #轮数.
    train_info["train_cost"].append(cost) #损失.
    train_info["train_accuracy"].append(train_acc)
  end_time = time.time()
  print("模型训练时间: %.8f 秒."%(end_time - start_time))     	#模型训练时间.

  #图形显示训练过程中损失和识别准确率变化情况.
  print("训练过程中损失(图15.5左)和识别准确率变化情况(图15.5右):")
  plt.figure()
  plt.plot(train_info["epoch"], train_info["train_cost"], "r")
  plt.xlabel('x轴 - 轮数', fontproperties='SimHei', fontsize=18)
  plt.ylabel('y轴 - 损失', fontproperties='SimHei', fontsize=18)
  plt.xticks(fontsize=16)
  plt.yticks(fontsize=16)
  plt.legend(['train_cost','line'], fontsize=16)
  plt.figure()
  plt.plot(train_info["epoch"],train_info["train_accuracy"],"b")
  plt.xlabel('x轴 - 轮数', fontproperties='SimHei', fontsize=18)
  plt.ylabel('y轴 - 识别准确率',fontproperties='SimHei',fontsize=18)
  plt.xticks(fontsize=16)
  plt.yticks(fontsize=16)
  plt.legend(['train_accuracy','line'],fontsize=16)
  plt.show()
  #4. 测试模型.
  print("2.测试模型")
  test_cor_pred = tf.equal(tf.argmax(y_predict,1),tf.argmax(y_real,1))
  # 计算识别准确率.
  test_accuracy = tf.reduce_mean(tf.cast(test_cor_pred, tf.float32))
  test_acc = test_accuracy.eval({x:mnist.test.images,y_real:mnist.test.labels})
  print("测试识别准确率:",test_acc)
  #5. 保存模型.
  save_path = saver.save(sess,model_path)
#启动会话.
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  #6. 读取模型.
  saver.restore(sess,model_path)
  #7. 验证模型.
  print("3.验证模型")
  #计算识别准确率.
  valid_cor_prediction = tf.equal(tf.argmax(y_predict,1),tf.argmax(y_real,1))
  valid_accuracy = tf.reduce_mean(tf.cast(valid_cor_prediction,tf.float32))
  print("验证识别准确率:",valid_accuracy.eval({x: mnist.validation.images,y_real:
 		mnist.validation.labels}))
  #输出验证结果.
  output = tf.argmax(y_predict,1)
  batch_xs,batch_ys = mnist.train.next_batch(2)
  res,pred_v = sess.run([output,y_predict],feed_dict={x:batch_xs})
  print("识别结果:",res)
  print("标签:",batch_ys)
  print("手写图像:")
  plt.imshow(batch_xs[0].reshape(-1,28))
  plt.show()
  plt.imshow(batch_xs[1].reshape(-1,28))
  plt.show()

