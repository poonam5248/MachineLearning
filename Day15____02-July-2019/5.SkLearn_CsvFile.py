import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

d=pd.read_csv('stock_market_data.csv')
print(d,"\n\n")

##test=d[['Date','Open','High','Low','Close','Volume']][0:4]
##print(test,"\n\n")
##
##train=d[['Date','Open','High','Low','Close','Volume']][4:]
##print(train,"\n\n")
##
##l=d[['Date']][4:]
##f=d[['Open','High','Low','Close','Volume']][4:]
##
##print(l,"\n\n")
##print(f,"\n\n")
##
##LR=LinearRegression()
##trained=LR.fit(f,l)
##res=trained.predict([['Date']][0:1])
##print(res)
##
d=np.array(d)
print(d)

f=d[:,0]
l=d[:,1:]

LR=LinearRegression()
t=LR.fit([f],l)
r=t.predict([f])
print(r)

