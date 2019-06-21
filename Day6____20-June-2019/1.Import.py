# Import

# 1.
import math

print(dir(math))

# 2.

print("\n\nThe Result is: ",math.sin(math.pi/2))

# 3.

import math as m
print("\n\nResult is",m.sin(m.pi/2))

# 4.

from math import pi, sin
print("\n\n",sin(pi/2))

#5.

from math import *
print("\n\n",sin(pi/2))

# 6.
a=int(input("\n\nEnter Input:"))
print(sqrt(a))

# 7.

a=[5,2]
b=[4,8]
d=sqrt((a[1]-a[0])**2+(b[1]-b[0])**2)
print("\n\nDistance is: ",d)

# 8.

a=[5,2]
b=[4,8]
d=sqrt((a[1]-a[0])**2+(b[1]-b[0])**2)
m=(b[1]-b[0])/(a[1]-a[0])
print("\n\nDistance is: ",d,"\nSlope is: ",m)

# 9.

a=[5,2]
b=[4,8]
def distance(a,b):
    d=sqrt((a[1]-a[0])**2+(b[1]-b[0])**2)
    return d
def slope(a,b):
    m=(b[1]-b[0])/(a[1]-a[0])
    return m
print("\n\nDistance is: ",distance(a,b),"\nSlope is: ",slope(a,b))

# 10.

##a=[5,2]
##b=[4,8]
D1=[]
S1=[]
def distance(a,b):
    d=sqrt((a[1]-a[0])**2+(b[1]-b[0])**2)
    return d
def slope(a,b):
    m=(b[1]-b[0])/(a[1]-a[0])
    return m
for i in range(0,2):
    a=int(input("\nEnter Number: \n"))
    b=int(input("Enter Number: \n"))
    D1.append(a)
    S1.append(b)
print("\nDistance is: ",distance(D1,S1),"\nSlope is: ",slope(D1,S1))






