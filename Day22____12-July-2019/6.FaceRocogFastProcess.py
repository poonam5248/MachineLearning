import face_recognition as fr
import cv2
v=cv2.VideoCapture(0)


name=['Poonam','Pushp']
i=fr.load_image_file('New Doc 2018-08-06_1.jpg')
j=fr.load_image_file('PIC PUSHP.jpg')
fL1=fr.face_locations(i)
##print(fL1)
fL2=fr.face_locations(j)
##print(fL2)
ke1=fr.face_encodings(i,fL1)[0]
##print(ke1)
ke2=fr.face_encodings(j,fL2)[0]
##print(ke2)
ke=[ke1,ke2]
##print(ke)

c=0
while(1):
    c=c+1
    r,im=v.read()
    if(c==4):
        img=im.copy()
        img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
        fL=fr.face_locations(img)


if(len(fL)>0):
    e=fr.face_encodings(img,fL)[0]
    f=fr.compare_faces(ke,e)
    print(f)
            # (right(index 0),top(index 1),left(index 2),bottom(index 3))
            
    x1=fL[0][3]*4
    y1=fL[0][0]*4
    x2=fL[0][1]*4 
    y2=fL[0][2]*4 
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),5)
c=0
r=True in f
if(r==True):
    ind=f.index(True)
    print(name[ind])
cv2.imshow('image',img)
k=cv2.waitKey(5)
if(k==ord('q')):
    cv2.destroyAllWindows()
break
