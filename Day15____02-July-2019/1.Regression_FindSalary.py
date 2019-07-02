# 1.

import math as m
F=[1,2,3,4]
L=[5,4,9,11]

for i in range(0,4):
    m=L[i]-L[i-1]/F[i]-F[i-1]

q=int(input("Enter Year: "))
print(m*q)







