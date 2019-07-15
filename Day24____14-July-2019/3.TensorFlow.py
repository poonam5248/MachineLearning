import tensorflow as tf
x=tf.placeholder(tf.float32)
b=tf.Variable(3.0,tf.float32)
w=tf.Variable(5.0,tf.float32)
y=w*x+b
init=tf.global_variables_initializer()
s=tf.Session()
s.run(init)
print(s.run(y,{x:[1,5,8]}))
