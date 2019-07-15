import tensorflow as tf
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
c=a+b
d=a*b
s=tf.Session()
print(s.run([c,d],{a:5.0,b:6.0}))
