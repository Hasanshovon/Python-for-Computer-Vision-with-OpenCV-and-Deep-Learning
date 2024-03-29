import cv2 
import numpy as np   
import matplotlib.pyplot as plt 

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),8)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

# define blank images
img = np.zeros((512,512,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20)  & 0xFF==27:
        break
cv2.destroyAllWindows()