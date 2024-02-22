import cv2
import time
cap=cv2.VideoCapture('5 sec video ad (sample 2).mp4')

while cap.isOpened():
    _,frame=cap.read()
    cv2.imshow('frame',frame)
    time.sleep(1/20)    
    if cv2.waitKey(1) & 0xFF==('q'):
        break
cap.release()
cv2.destroyAllWindows()