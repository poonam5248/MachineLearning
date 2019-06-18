U=['Poonam','Nikhil','Kiara','Priyank']
P=[5248,4852,5842,4258]
#Run three times use count 
count=0
while True:
    while(count<3):
        username=input("Username: ")
        r = username in U
        if(r==True):
            print("Welcome")
            b=int(input("Password: "))
            ind=U.index(username)
            if(b==P[ind]):
                print("Password Correct")
                count=0 
                break
            else:
                print("Password Incorrect")
                count=count+1
        else:
            print("Invalid username")
    if(count==3):
        print("You are blocked")
        count=0

