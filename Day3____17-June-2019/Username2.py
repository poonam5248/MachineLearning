U=['Poonam','Nikhil','Kiara','Priyank']
P=[5248,4852,5842,4258]

while True:
    username=input("Username: ")
    r = username in U
    if(r==True):
        print("Welcome")
        b=int(input("Password: "))
        ind=U.index(username)
        if(b==P[ind]):
            print("Password Correct")
            break
        else:
            print("Password Incorrect")
    else:
        print("Invalid username")
