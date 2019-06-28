# 1.

print("Output of 1st program is: ")
import pandas as pd
d=pd.DataFrame([5,2,4,8])
print(d)
print(d[0])

# 2.

print("\n\nOutput of 2nd Program is: ")
d=pd.DataFrame({'a':[5,2,4,8]})
print(d)

# 3.

print("\n\nOutput of 3rd Program is: ")
print(d['a'][1])

# 4.

print("\n\nOutput of 4th Program is: ")
d=pd.DataFrame({'a':[5,2,4,8],'b':[4,8,5,2]})
print(d)

# 5.

print("Output of 5th Program is: ")
print(d['a'][1])
print("\n",d['b'][1])

# 6.

print("Output of 6th Program is: ")
D=d.T
print(D,"\n")
print(D[1],"\n")
print("Shape is: ",D.shape)
print("Dimension is: ",D.ndim)
print("Size is: ",D.size)

# 7.

print("\n\nOutput of 7th Program is: ")
d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['abc','xyz'])
print(d)

# 8.

print("\n\nOutput of 8th Program is: ")
print(d['b'][1])

print(d['b'][0])
print(d['c'][0])
print(d['c'][1])
print(d[['b','c']],"\n")
d['e']=d['c']+d['d']
print(d,"\n")
m=d[{'a','b'}]
print(m,'\n')
print("Type of m is: ",type(m))

# 9.

print("\n\nOutput of 9th Program is: ")
print(d[:],"\n")
print(d[0:1],"\n")
print(d[1:2],"\n")
print(d['a'][0:2],"\n")
print(d['a'][0:1],"\n")
print(d['a':'b'][0:1],"\n")
print(d[0:2][0:1],"\n")
print(d[{'a','b'}][0:1],"\n")
print(d[['a','b']][0:1],"\n")
print(d.T)

# 10.
##
##d1=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['a','b'])
##d2=pd.DataFrame([[4,8,5,2],[45,2,4,8]],columns=['a','b','c','d'],index=['a','b'])
##s=d.add(d1,d2)
##print(s)

# 11.

import numpy as np
print("Output of 11th Program is : ")
a=np.arange(50).reshape(5,10)
d=pd.DataFrame(a)
print(d,"\n\n")

d=pd.DataFrame(a,columns=['a','b','c','d','e','f','g','h','i','j'],index=['a','b','c','d','e'])
print(d,"\n")
print(d[['b','c']][0:2],"\n")
print(d[['b','c']][0:],"\n")
print(d[['b','c']][0:4],"\n")
print(d[['b','c']][0:2].sum(),"\n")
print(d.columns,"\n")
print(d.index,"\n")
print(d.iloc(0),"\n")
print(d[0:1],"\n")
print(d.iloc[0:3])



      


