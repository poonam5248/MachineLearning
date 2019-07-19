import torch as th
import numpy as np

def n():
    a=th.randn(1)
    w=a
    print(w)
    b=th.randn(1)
    y=b
    print(y)
    b=int(input("Enter Number:"))
    b=th.tensor(b)
    print(b)
n()
