from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

d=pd.read_csv('4.Iris.csv')
print(d,"\n\n")

f=d[['Sepal Length','Sepal Width','Petal Length','Petal Width']]
l=d['Species']
clf=GaussianNB()
train=clf.fit(l,f)
resn=train.predict([[4.6,3.1,1.5,0.2]])
print(resn)


f=d[['Sepal Length','Sepal Width','Petal Length','Petal Width']]
l=d['Species']
clf=DecisionTreeClassifier()
t=clf.fit(f,l)
resd=t.predict([[5.9,3,4.2,1.5]])
print(resd)
