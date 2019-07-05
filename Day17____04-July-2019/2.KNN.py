import math as m
D=[[],[]]
F=[[],[]] # F is that in which data is copied
f=[[40,60],[50,50],[70,35],[35,65],[70,70],[70,90],[80,95],[80,75],[90,90]] # f is the data
# x1=40 and y1=60
l=['P','P','P','P','G','G','G','G','G']
f1=f.copy() # f1 for copy
L=l.copy()
t=[[60,45]]  # x2=60, y2=45
cat=list(set(l))
print(cat)

while(len(cat)!=len(F)):
    F.append([])
    D.append([])
for i in range(len(cat)): # cat has only two values i.e., 0 And 1
    while cat[i] in L:
        ind=L.index(cat[i])
        F[i].append(f1[ind])
        del(L[ind],f1[ind])
print(F)

s=[]

for k in range(len(F)):
    for j in range(len(F[k])):
        d=m.sqrt((F[k][j][1]-t[0][1])**2+(F[k][j][0]-t[0][0])**2)
        D[k].append(d)
print(D)
n=int(input("Enter the value of k: "))
for m in range(len(D)):
    D[m].sort()
    s.append(sum(D[m][0:n]))
print(cat[s.index(min(s))])

    
        
            
    
        
        
        
