
from sklearn.linear_model import LinearRegression
f=[[1,10,50],[2,15,100],[3,18,200],[4,25,500]]
l=[5,8,9,13]
LR=LinearRegression()
trained=LR.fit(f,l)
res=trained.predict([[20,450,2000]])
print(res)
