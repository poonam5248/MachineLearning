from sklearn.tree import DecisionTreeClassifier
f=[[150,1],[180,1],[120,0],[100,0]]
l=['A','A','O','O']
clf=DecisionTreeClassifier()
t=clf.fit(f,l)
r=t.predict([[180,1],[120,0],[150,1],[130,0]])
print(r)
