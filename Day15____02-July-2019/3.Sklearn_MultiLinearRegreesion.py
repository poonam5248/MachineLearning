
# Multiple Linear Regreesion

from sklearn.linear_model import LinearRegression
f=[[1,10],[2,15],[3,18],[4,25]]
l=[5,8,9,11]
LR=LinearRegression()
trained=LR.fit(f,l)
res=trained.predict([[20,50]])
print(res)
