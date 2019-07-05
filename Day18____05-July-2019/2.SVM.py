from sklearn.svm import SVC
f=[[40,60],[50,50],[70,35],[35,65],[70,70],[70,90],[80,95],[85,75],[90,90]]
l=['P','P','P','P','G','G','G','G','G']

clf=SVC(kernel="linear",C=2,gamma=0.3)
t=clf.fit(f,l)
res=t.predict([[60,45],[65,40],[85,90],[90,80],[60,65]])
print(res)
