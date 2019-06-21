# Libraries (Collection of Functions)

## math
## OS(SYS)
## Time
## Datetime
## random
## request
## smtp


# 1.
##import os
##print(os.name)
##print(os.path)
##print(os.getcwd()) # Get current working directory
##

# 2.

##import os
##print(os.name)
##print(os.path)
##cd=os.getcwd()
##print(cd)
##ls=os.listdir()
##print(ls)
##r='F:\Machine Learning' in ls
##if(r==True):
##    ind=ls.index('F:\Machine Learning')
##path=cd+'\\'+ls[ind]
##os.chdir(path) # Change directory
##print(cd)
##print(os.listdir())

# 3.

##import time
##print("Hello")
##time.sleep(5)
##print("How are you?")

# 4.
##import time
##t1=time.time()
##for i in range(1,10):
##    print(i)
##    time.sleep(1)
##t2=time.time()
##print(t2-t1)

# 5.
##
##def sleep_min(t):
##    time.sleep(60*t)
##t1=time.time()
##for i in range(1,10):
##    print(i)
##    sleep_min(1)
##t2=time.time()
##print(t2-t1)

# 6.

##import time
##
##print(time.ctime())
##t=time.ctime()
##print(t,type(t))
##print(t[11:19],type(t))

# 7.

##import time
##u=input("Enter your Question: ")
##if(u=="What is The time: "):
##    t=time.ctime()
##    print(t[11:19],type(t))

# 8.

##import time
##q='1'
##while(q!='*'):
##    u=input("Enter Your Question: ")
##    if(u=='Hii'):
##        print('Hello')
##    elif(u=='Hello'):
##        print("Hii")
##    elif(u=="What is Your Name "):
##        print("Poonam")
##    elif(u=="What is the Time "):
##        t=time.ctime()
##        print(t[11:19])
##    elif(u=='Thank You') or (u=="Bye"):
##        print("It was Nice Talking with You")
##    else:
##        print("I am Trained for this yet")
##    q=u
##    


# 9. Random
##
##import random as r
##d=r.random()
##print(d)
##
### 10.
##
##d=r.randint(0,100)
##print(d)

# 11.
import random as r
d=r.randrange(0,100,18)
print(d)

# 12.
a=[4,8,5,2,1,0]
d=r.choice(a)
print(d)

r.shuffle(a)

print(a)







































