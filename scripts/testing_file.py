import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #red color detection
    low_red=np.array([161,155,84])
    upper_red=np.array([179,255,255])
    redMask=cv2.inRange(hsv_frame,low_red,upper_red)
    red=cv2.bitwise_and(frame,frame,mask=redMask)
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',red)

    if cv2.waitKey(10)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
 
