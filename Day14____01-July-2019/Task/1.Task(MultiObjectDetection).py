import cv2

face=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
eye=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')
cat=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalcatface.xml')
v=cv2.VideoCapture(0)

while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(j)
    for (fx,fy,fw,fh) in faces:
        cv2.rectangle(i,(fx,fy),(fx+fw,fy+fh),(0,0,255),5)
        eyes=eye.detectMultiScale(j)

        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(i,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)
            cats=cat.detectMultiScale(j)
            for(cx,cy,cw,ch) in cats:
                cv2.rectangle(i,(cx,cy),(cx+cw,cy+ch),(255,0,0),5)
        
    cv2.imshow('img',i)
    k=cv2.waitKey(10)   
    if(k==ord('q')):
        break
v.release()
cv2.destroyAllWindows()

