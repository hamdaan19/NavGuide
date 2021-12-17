import cv2

ss=cv2.CascadeClassifier("pedestrianLights\classifier\cascade.xml")
cap=cv2.VideoCapture(0)

cap.set(4,480)
cap.set(3,360)

while True:
    ret,img = cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('screen',img)
    Screen=ss.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in Screen:
        print("Traffic signal detected")
    key=cv2.waitKey((30))
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
