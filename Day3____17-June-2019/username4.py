U=['Poonam','Nikhil','Kiara','Priyank']
P=[5248,4852,5842,4258]
while True:
    op=(input("Enter your choice: "))
    if(op=='*'):
        print(U)
        print(P)
    elif(op=='1'):
        print("You have successfully choosen signup option")
        a=input("Enter your username: ")
        b=input("Enter your password: ")
        U.append(a)
        P.append(b)

    elif(op=='2'):
        print("You have successfully choosen sign in option")
    #Run three times use count 
        count=0
        w=1
        while w:
            while(count<3):
                    username=input("Enter your Username: ")
                    r = username in U
                    if(r==True):
                        print("Welcome")
                        b=int(input("Enter Your Password: "))
                        ind=U.index(username)
                        if(b==P[ind]):
                            print("Your Password is Correct")
                            count=0 
                            break
                        else:
                            print("Password is Incorrect")
                            count=count+1
                    else:
                        print("Invalid username")
            if(count==3):
                print("You are blocked")
                count=0
                w=int(input("Do you want to continue If Yes Then \n Press 1 otherwise Press 0"))
    elif(op=='@'):
        exit()
    else:
        print("You have pressed a wrong key")

