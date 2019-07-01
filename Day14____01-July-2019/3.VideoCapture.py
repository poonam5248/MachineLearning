
import cv2 as cv
v=cv.VideoCapture(0)
while(1):
    r,i=v.read() # r is the return type of image 
    j=cv.cvtColor(i,cv.COLOR_BGR2GRAY)
    r,g=cv.threshold(j,127,255,0) # in this r return threshold
    cv.imshow('digital',g)
    cv.imshow('gray',j)
    cv.imshow('img',i)
    k=cv.waitKey(3)
    if(k==ord('q')):
        cv.destroyAllWindows()
        v.release()
        break
