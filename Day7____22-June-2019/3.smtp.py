import smtplib as s

g=s.SMTP("smtp.gmail.com",587)
a=input("Enter sender's Email Id:")
b=input("Enter Password:")
f=open(r"F:\Machine Learning\Day7____22-June-2019\3.Email.txt",'r')
c=f.readlines()
f.close()
h=open(r"F:\Machine Learning\Day7____22-June-2019\4.Message.txt",'r')
d=h.read()
h.close()
print("Start")
g.starttls() # tls=transport layer security
g.login(a,b)
print("Login Successfully") 
g.sendmail(a,c,d)
g.close()
print("End")
