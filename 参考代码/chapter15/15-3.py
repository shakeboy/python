import tensorflow as tf
#定义变量.
a = tf.Variable(3)
b = tf.Variable(4)
c = tf.add(a,b)
#变量初始化.
init_op = tf.global_variables_initializer()
#创建交互式会话.
sess = tf.InteractiveSession()
sess.run(init_op)
#运行并输出变量.
print('c =',sess.run(c))
