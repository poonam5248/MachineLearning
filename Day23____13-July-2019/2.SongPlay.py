import vlc
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

er=load_model(r'F:\Machine Learning\Day23____13-July-2019\_mini_XCEPTION.106-0.65.enc')
fd=cv2.CascadeClassifier(r'F:\Machine Learning\Day23____13-July-2019\haarcascade_frontalface_default.xml')

em=['angry','disgust','scared','happy','sad','surprised','neutral']

a=vlc.MediaPlayer(r'F:\Machine Learning\Day23____13-July-2019\SongsList\Happy\Hum Teri Mohabbat Mein-Kumar Sanu__Raag.Me__.mp3')
v=cv2.VideoCapture(0)

while(1):
    r,i=v.read()
    cv2.imshow('image',i)
    k=cv2.waitKey(5)
    

    if(k==ord('c')):
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        f=fd.detectMultiScale(j,1.3,5)
        if(len(f)==1):
            for(x,y,w,h) in f:
                g=j[y:y+h,x:x+w]
                g=cv2.resize(g,(48,48))
                g=g.astype('float')/255.0
                g=img_to_array(g)
                
                g=np.expand_dims(g,axis=0)
                print(g)
                p=er.predict(g)[0]
                ind=np.argmax(p)
                print(em[ind])

                if(em[ind]=='happy'):
                    a.play()

    if(k==ord('q')):
        cv2.destroyAllWindows()
        v.release()
        break

        
