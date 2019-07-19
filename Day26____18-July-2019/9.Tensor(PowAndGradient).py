import torch as th
from torch.autograd import Variable
a=4
a=th.tensor(a)
print(a.pow(4))


##b=8
##print(b)
##c=th.autograd.variable(a,requires_grad=False)
##print(c)



b=Variable(a,requires_grad=False)
print("\n\n",b)
n=th.autograd.Variable()
print(n)

