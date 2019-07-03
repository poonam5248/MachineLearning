from sklearn.tree import DecisionTreeClassifier
f=[[150,1],[180,1],[120,0],[100,0],[250,2],[300,2]]
l=['A','A','O','O','W','W']
clf=DecisionTreeClassifier()
t=clf.fit(f,l)
r=t.predict([[180,1],[120,0],[150,1],[130,0],[250,2],[300,2]])
print(r)
