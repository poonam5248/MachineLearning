import cv2 as cv
v=cv.VideoCapture(0)

while(1):
    r,i=v.read()
    cv.circle(i,(300,300),50,(0,0,255),5) # in this r return threshold
##  cv.circle(i,(300,300),50,(0,0,255),50)
##  cv.circle(i,(300,300),50,(0,0,255),-5)
    cv.imshow('img',i)
    k=cv.waitKey(5)
    if(k==ord('q')):
        cv.destroyAllWindows()
        v.release()
        break
