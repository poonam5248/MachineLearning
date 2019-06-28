import numpy as np
import pandas as pd
a=np.arange(50).reshape(5,10)
d=pd.DataFrame(a)
d=pd.DataFrame(a,columns=['a','b','c','d','e','f','g','h','i','j'],index=['a','b','c','d','e'])
d.to_csv('abcd.csv')
print(d)

d=pd.read_csv('abcd.csv')
print(d)
