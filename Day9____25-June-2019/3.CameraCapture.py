import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
##    print("ret= ",ret)
##    print("Frame= ",frame)

    cv2.imshow('Frame', frame)
    if(cv2.waitKey(5)==ord('s')):
        cv2.imwrite("Image2.jpg",frame)
        continue
    if(cv2.waitKey(5)==ord('q')):
        cv2.destroyAllWindows()
        break
print("All Done")
