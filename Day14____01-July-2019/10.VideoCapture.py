import cv2
fd=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
v=cv2.VideoCapture(0)

while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j)

    for (x,y,w,h) in f:
        cv2.rectangle(i,(x,y),(x+y,w+h),(0,0,255),5)
        t=i[y:y+h,x:x+w,:]
        cv2.imshow('tval',t)
        cv2.imshow('img',i)
        k=cv2.waitKey(5)
        if(k==ord('q')):
            cv2.destroyAllWindows()
            v.release()
            break
