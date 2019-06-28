# 1.

import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[5,6,7,8]
plt.figure(0)
plt.plot(x,y)
a=[7,8,9,10]
b=[5,6,4,9]
p=[4,5,6,7]
q=[2,7,8,9]
plt.figure(1)
plt.plot(a,b,p,q)

plt.show()

# 2.

import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[5,6,7,8]
plt.figure(0)
plt.plot(x,y,'r')
a=[7,8,9,10]
b=[5,6,4,9]
plt.title("Hello")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
p=[4,5,6,7]
q=[2,7,8,9]
plt.figure(1)
plt.plot(a,b,'g',p,q,'b')
plt.plot(a,b,'g^',p,q,'b')  # ^ called as scattered graph
plt.plot(a,b,'g^',p,q,'.')
plt.plot(a,b,'--',p,q,'--')
plt.plot(a,b,'--g',p,q,'--b')
plt.title("Hii....")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
##plt.show()

# 4.

import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[5,6,7,8]
plt.figure(0)
plt.plot(x,y,'r')
a=[7,8,9,10]
b=[5,6,4,9]
plt.title("Hello")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
p=[4,5,6,7]
q=[2,7,8,9]
plt.figure(1)
#plt.plot(a,b,'g',p,q,'b')
##plt.plot(a,b,'g^',p,q,'b')  # ^ called as scattered graph
##plt.plot(a,b,'g^',p,q,'.')
##plt.plot(a,b,'--',p,q,'--')
plt.title("Hii....")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(a,b,'--g',p,q,'^b')
plt.legend(['pressure','temperature'])

plt.show()

# 5.

import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[5,6,7,8]
plt.figure(0)
plt.plot(x,y,'r')
a=[7,8,9,10]
b=[5,6,4,9]
plt.title("Hello")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
p=[4,5,6,7]
q=[2,7,8,9]
plt.figure(1)
#plt.plot(a,b,'g',p,q,'b')
##plt.plot(a,b,'g^',p,q,'b')  # ^ called as scattered graph
##plt.plot(a,b,'g^',p,q,'.')
##plt.plot(a,b,'--',p,q,'--')
plt.title("Hii....")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(a,b,a,b,'*')
plt.legend(['pressure','temperature'])

plt.show()

# 6.

import matplotlib.pyplot as plt
x=[10,4,5,3]
y=[5,3,8,1]
##plt.figure(0)
##plt.plot(x,y,'r')
##a=[7,8,9,10]
##b=[5,6,4,9]
##plt.title("Hello")
##plt.xlabel("X-axis")
##plt.ylabel("Y-axis")
##p=[4,5,6,7]
##q=[2,7,8,9]
plt.figure(1)
# plt.plot(a,b,'g',p,q,'b')
##plt.plot(a,b,'g^',p,q,'b')  # ^ called as scattered graph
##plt.plot(a,b,'g^',p,q,'.')
##plt.plot(a,b,'--',p,q,'--')
plt.title("Hii....")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.bar(x,y)
plt.legend(['pressure','temperature'])

plt.show()


# 7.

import matplotlib.pyplot as plt
x=['a','b','c','d']
y=['u','v','w','x']
plt.figure(0)
##plt.plot(x,y,'r')
a=[7,8,9,10]
b=[5,6,4,9]
##plt.title("Hello")
##plt.xlabel("X-axis")
##plt.ylabel("Y-axis")
##p=[4,5,6,7]
##q=[2,7,8,9]
plt.figure(1)
##plt.plot(a,b,'g',p,q,'b')
##plt.plot(a,b,'g^',p,q,'b')  # ^ called as scattered graph
##plt.plot(a,b,'g^',p,q,'.')
##plt.plot(a,b,'--',p,q,'--')
plt.title("Hii....")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.bar(x,y,a,b)
plt.show()

# 8.

import matplotlib.pyplot as plt
x=['a','b','c','d']
y=['u','v','w','x']
##plt.figure(0)
##plt.plot(x,y,'r')
##a=[7,8,9,10]
##b=[5,6,4,9]
##plt.title("Hello")
##plt.xlabel("X-axis")
##plt.ylabel("Y-axis")
##p=[4,5,6,7]
##q=[2,7,8,9]
plt.figure(1)
# plt.plot(a,b,'g',p,q,'b')
##plt.plot(a,b,'g^',p,q,'b')  # ^ called as scattered graph
##plt.plot(a,b,'g^',p,q,'.')
##plt.plot(a,b,'--',p,q,'--')
plt.title("Hii....")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.bar(x,y,a,b)
plt.show()

# 9.


import matplotlib.pyplot as plt
u=[5,6,7,3]
v=[2,6,8,90]
plt.plot(u,v,'--')
plt.plot(u,v,u,v,'o')
plt.legend(['ab','pq','uv'])

plt.bar(u,v)
plt.show()

# 10.

x=[5,2,4,8]
y=[9,8,5,4]
plt.figure(0)
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Imp")
plt.plot(2,2,2)
plt.bar(x,y)
plt.subplot(2,2,4)
plt.plot(x,y,'*')
##plt.scatter(x,y)
plt.show()

# 11.

import pandas as pd
d=pd.read_csv(r"F:\Machine Learning\Day12___28-June-2019\4.Iris.csv")
u=d[['a']]
v=d[['b']]
plt.plot(u,'*g')
plt.plot(v,'^r')
x=d[['c']]
y=d[['d']]
plt.plot(x,'.b')
plt.plot(y,'--y')
plt.show()




























