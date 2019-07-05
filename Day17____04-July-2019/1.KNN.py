
from sklearn.neighbors import KNeighborsClassifier
f=[[40,60],[50,50],[70,35],[35,65],[70,70],[70,90],[80,95],[85,75],[90,90]]
l=['P','P','P','P','G','G','G','G','G']

##test=[[60,45],[65,40],[85,35],[40,80],[60,65]]
clf=KNeighborsClassifier()
t=clf.fit(f,l)
res=t.predict([[60,45],[65,40],[85,90],[90,80],[60,65]])
print(res)

# above 70% is in Good Category
