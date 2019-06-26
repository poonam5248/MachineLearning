import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    print("ret= ",ret)
    print("Frame= ",frame)

    cv2.imshow('Frame', frame)
    cv2.waitKey(5)
