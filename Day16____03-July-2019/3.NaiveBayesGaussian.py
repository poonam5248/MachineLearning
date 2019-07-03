from sklearn.naive_bayes import GaussianNB
f=[[150,1],[180,1],[120,0],[100,0]]
l=['A','A','O','O']
clf=GaussianNB()
t=clf.fit(f,l)
r=t.predict([[180,1],[120,0],[150,0],[130,0]])
print(r)
