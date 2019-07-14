import face_recognition as fr
import cv2
import pandas as pd
d=pd.read_csv('F:\Machine Learning\Day22____12-July-2019\Log1.csv')
v=cv2.VideoCapture(0)

while(1):
    r,img=v.read()
    fL=fr.face_locations(img)
    if(len(fL)>0):
        e=fr.face_encodings(img,fL)[0]
        print(e)
        # (right(index 0),top(index 1),left(index 2),bottom(index 3))
        if(str(e) in d):
            print("Data Exists")
        else:
            print("Find New Data")
            a=input("Enter Your Name: ")
            f=open(r'F:\Machine Learning\Day22____12-July-2019\Log1.csv','a')
            data=(a+str(e))
            f.write(data)
            f.close()
        x1=fL[0][3]
        y1=fL[0][0]
        x2=fL[0][1] 
        y2=fL[0][2] 
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),5)

    cv2.imshow('image',img)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
