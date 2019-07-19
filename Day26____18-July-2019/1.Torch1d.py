import torch as th
a=th.zeros(5)
b=th.ones(4)
c=th.eye(3)
print(a)
print(b)
print(c)

a=a.type(th.int32)
