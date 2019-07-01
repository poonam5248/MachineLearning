import cv2 as cv
v=cv.VideoCapture(0)
b=0
r,m=v.read()
while(1):
    r,i=v.read()
    i=i+b
    d=m-i
    j=cv.cvtColor(d,cv.COLOR_BGR2GRAY)
    r,g=cv.threshold(j,127,255,0) # in this r return threshold
    
    cv.imshow('bs',d)
    cv.imshow('digital',g)
    cv.imshow('gray',j)
    cv.imshow('img',i)
    k=cv.waitKey(5)
    if(k==ord('q')):
        cv.destroyAllWindows()
        v.release()
        break
