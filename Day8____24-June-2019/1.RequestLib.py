# 1.

import requests as r
import time
while True:
    data=r.get(r"http://indianiotcloud.com/retrieve.php?id=ZIZ1CVNOZI5TFDSQEB2U")
    d=data.json()
    print(d['result'][0]['field1'])
    time.sleep(1)

# 2.

import requests as r
import time
while True:
    d=input("Enter Your Data to Send: ")
    data=r.get(r"http://indianiotcloud.com/retrieve.php?id=ZIZ1CVNOZI5TFDSQEB2U&field1="+d+"&field2=0&field3=0&field4=0")
    d=data.json()
    print(d['result'][0]['field1'])
    time.sleep(1)



    

    
