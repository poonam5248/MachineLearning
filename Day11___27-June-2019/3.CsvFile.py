import pandas as pd
import numpy as np
a=pd.read_csv('abcd.csv')
print(a)
print(a.columns)
b1=a[['a','b','c','d',]][5:50]
b2=a[['a','b','c','d',]][55:100]
b3=a[['a','b','c','d',]][105:150]
train=pd.concat([b1,b2,b3])
print(train)

d1=a[['a','b','c','d',]][0:5]
d2=a[['a','b','c','d',]][50:55]
d3=a[['a','b','c','d',]][100:105]
test=pd.concat([d1,d2,d3])
print(test)
e=a[['e']][0:150]
print(e)



