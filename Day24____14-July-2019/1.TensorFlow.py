import tensorflow as tf
a=tf.constant(5.0,tf.float32)
b=tf.constant(4.0,tf.float32)
c=a+b
d=a*b
s=tf.Session()
print(s.run([c,d]))
