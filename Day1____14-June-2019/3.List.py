#LISTS


a=[100,'Hello','200','Poonam52','Nikhil',48]
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])

a.append(10)
print(a)

a.insert(2,50) #a.insert(loc,data)
print(a)

a.remove('200')
print(a)

a.pop()
print(a)

a.pop(len(a)-1)
print(a)

del a[2]
print(a)

b=a.copy()
print("b=",b)

c=a
print("c=",c)

print(id(a))
print(id(b))
print(id(c))

print("a=",a)
print("b=",b)
print("c=",c)

list=[1,[5,3,(8,[5,19]),23,7,3],5,4,1]
print(list[0])
print(list[2:])
print(list[len(list)-2:])
print(list[1][0])
print(list[1][2][0])
print(list[1][2][1][0])
##list[1][2][0]=100
##print(list)              Not Possible to change in tuple

list[1][2][1][0]=15
print(list)

r= 5 in list
print(r)

ind=list.index(5)
print(ind)

list.clear()
print(list)





