import torch as th
m=th.arange(5,50)
print(m)
a=len(m.shape)
print(a)

print(m.dim())
n=th.reshape(m,(15,3))

print(n)
print(n.shape)
print(n.dim())
b=th.reshape(m,(3,3,5))
print(b)
print(b.shape)
print(b.dim())



p=th.exp(th.tensor(0,dtype=th.float32))
print(p)

q=th.tensor([1,5,3],device='cpu') # cpu or gpu_name(Two Types)(Quda is main)
print(q)


