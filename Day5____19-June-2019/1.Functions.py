# 1st category
def tn():
    print("TechieNest")
tn()

# 2nd Category

def abc(l,m,n,t):
    for i in range(0,l):
        print("Hello",m+n-i,str(t)+' '+'Yes')
abc(9,3,6,'Qwerty')

# 3rd Category

def abc():
    a=input("Enter Your Name: ")
    b=a*3
    return(b)
w=abc()
print(w)

#
def abc():
    a=int(input("Enter Your Data: "))
    b=a*3
    return(a,b,b**2,"it was Good")
w=abc()
print(w)

#
def abc():
    a=int(input("Enter Your Data: "))
    b=a*3
    return(a,b,b**2,"it was Good")
a,b,c,d=abc()
print(a,b,c,d)

# 4th Category

def abc(p,q,op):
    if(op==1):
        r=p+q
    elif(op==2):
        r=p-q
    elif(op==3):
        r=p*q
    elif(op==4):
        r=p/q
    else:
        r="Wrong Choice"
    return r
z=1
while(z!=10):
    x=int(input("Enter 1st value:"))
    y=int(input("Enter 2nd value:"))
    z=int(input("Enter Your choce 1>+ 2>- 3>* 4>/"))

    res=abc(x,y,z)
    print(res)
    
