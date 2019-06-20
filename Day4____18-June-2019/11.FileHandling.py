n=int(input("Enter the number of details you want to add:"))
for i in range(n):
    a=input("Enter Your Name:")
    e=len(a)
    if(e>3):
        pass
    else:
        a=input("Please Enter Your Full Name more than 3 characters:")

    b=input("Enter Your Email:")
    g='@' in b
    if(g==True):
        pass
    else:
        b=input("Please Enter Your Valid Email:")
    c=input("Enter your Mobile Number:")
    h=len(c)
    if(h==10):
        pass
    else:
        c=input("Please Enter 10 digit Number:")
    d=input("Enter Password: ")
    k=len(d)
    if(k==6):
        pass
    else:
        d=input("Please Enter 6 digit Password: ")


        f=open(r"F:\Machine Learning\log1.txt",'a')
        data=a+'\t'+b+'\t'+c+'\t'+d+'\n'
        f.write(data)
        f.close()
        
