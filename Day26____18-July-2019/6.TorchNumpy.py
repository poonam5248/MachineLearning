import torch as th
import numpy as np
a=np.array([1,5,9,3])
f=th.from_numpy(a)
print(f)
b=f.numpy()
