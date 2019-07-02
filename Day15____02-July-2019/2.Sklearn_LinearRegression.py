# scikit

#import sklearn.linear_model
 
from sklearn.linear_model import LinearRegression
f=[[1],[2],[3],[4]]
l=[5,8,9,11]
LR=LinearRegression()
trained=LR.fit(f,l)
res=trained.predict([[8],[3],[5],[1]])
print(res)
