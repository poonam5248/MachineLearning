
import cv2 as cv
v=cv.VideoCapture(0)

while(1):
    r,i=v.read()
    cv.rectangle(i,(50,50),(200,200),(0,0,255),5) # in this r return threshold
##  cv.rectangle(i,(50,50),(200,200),(0,0,255),50)
##  cv.rectangle(i,(50,50),(200,200),(0,0,255),-1)
    cv.imshow('img',i)
    k=cv.waitKey(5)
    if(k==ord('q')):
        cv.destroyAllWindows()
        v.release()
        break
