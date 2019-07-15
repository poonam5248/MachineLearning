import tensorflow as tf
x=tf.placeholder(tf.float32)
m=3.0
n=5.0
for i in range(0,5):
    
    b=tf.Variable(m,tf.float32)
    w=tf.Variable(n,tf.float32)
    r=tf.placeholder(tf.float32)
    y=w*x+b
    d=tf.reduce_sum(tf.square(r-y))
    init=tf.global_variables_initializer()
    opt=tf.train.GradientDescentOptimizer(0.001)
    s=tf.Session()
    s.run(init)
    t=opt.minimize(d)
    for i in range(0,100):
        print(s.run([y,d,t],{x:[1,5,8],r:[10,30,40]}))
        print(s.run([w,b]))
        m=b
        n=w
