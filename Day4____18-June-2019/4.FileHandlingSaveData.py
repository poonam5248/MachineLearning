# Append Mode
q=1
while(q):
    a=input("Enter Your Name: ")
    b=input("Enter Your Email: ")
    c=input("Enter Password: ")
    d=input("Enter Your Phone Number: ")

    f=open(r"F:\Machine Learning\Day4____18-June-2019\log.txt",'a')
    data=a+'\t'+ b+'\t'+ c+'\t'+ d+ '\n'

    f.write(data)
    q=int(input("Do you want to Continue Press 1 for Yes And Press 2 for No"))
    f.close()
