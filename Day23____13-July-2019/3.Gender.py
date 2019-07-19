import face_recognition as fr
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
er=load_model(r'F:\Machine Learning\Day23____13-July-2019\gender_mini_XCEPTION.21-0.95.hdf5')
print(er)
fd=cv2.CascadeClassifier(r'F:\Machine Learning\Day23____13-July-2019\haarcascade_frontalface_default.xml')
v=cv2.VideoCapture(0)
em=['female','male']
while(1):
    
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)    
    f=fd.detectMultiScale(j,1.3,5)
    if(len(f)==1):
        for (x,y,w,h) in f:
            t=j[y:y+h,x:x+w]
            t=cv2.resize(t,(64,64))
            t=t.astype('float')/255.0
            t=img_to_array(t)
            t=np.expand_dims(t,axis=0)
            print(t)
            p=er.predict(t)[0]
            ind=np.argmax(p)
            print(em[ind])
            cv2.imshow('image',i)
            k=cv2.waitKey(5)
            if(k==ord('q')):
                cv2.destroyAllWindows()
                v.release()
                break
        
