import tensorflow as tf
#占位符.
a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)
#构建计算图.
c = a * 10 + b
#创建会话.
sess = tf.InteractiveSession()
#方式一：通过eval()方法给a、b传值.
print("c =",c.eval({a:1,b:2}))     	#0维张量.
print("c =",c.eval({a:[1],b:[2]}))   	#1维张量.
print("c =",c.eval({a:[[1,2],[3,4]],b:[[1,2],[3,4]]}))	#2维张量.
#方式二：通过feed_dict()方法给a,b传值.
print("c =",sess.run(c,feed_dict={a:1,b:2}))    	#0维张量.
print("c =",sess.run(c,feed_dict={a:[1],b:[2]}))  	#１维张量.
print("c =",sess.run(c,feed_dict={a:[[1,2],[3,4]],b:[[1,2],[3,4]]}))
	#2维张量.
