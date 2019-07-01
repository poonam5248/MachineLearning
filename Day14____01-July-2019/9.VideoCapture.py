import cv2 as cv
fd=cv.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
v=cv.VideoCapture(0)

while(1):
    r,i=v.read()
    j=cv.cvtColor(i,cv.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j)

    for (x,y,w,h) in f:
        
        cv.rectangle(i,(x,y),(x+y,w+h),(0,0,255),5)
    ##  cv.rectangle(i,(50,50),(200,200),(0,0,255),50)
    ##  cv.rectangle(i,(50,50),(200,200),(0,0,255),-1)
        cv.imshow('img',i)
        k=cv.waitKey(5)
        if(k==ord('q')):
            cv.destroyAllWindows()
            v.release()
            break
