

import numpy as np
import cv2



def mousecall(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        zoomin(x,y)

    elif event == cv2.EVENT_RBUTTONDBLCLK:
        zoomout()

def mousenone(event,x,y,flags,param):

    return 0
    
def zoomin(x,y):
    
    cv2.setMouseCallback('frame', mousenone)
    
    while(True):
        ret, img = cap.read()
    
        x1 = x - 160
    
        if x1 < 0:
            x1 = 0
    
        x2 = x + 160
    
        if x2 > 640:
            x2 = 640
        
        y1 = y - 96
    
        if y1 < 0:
            y1 = 0
    
        y2 = y + 96
        
        if y2 > 480:
            y2 = 480
    
        pts1 = np.float32([[x1,y1],[x2,y1],[x1,y2],[x2,y2]])
        pts2 = np.float32([[0,0],[320,0],[0,192],[320,192]])

        M = cv2.getPerspectiveTransform(pts1,pts2)

        dst = cv2.warpPerspective(img,M,(320,192))
            
        cv2.imshow('frame',dst)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            zoomout()
            break

def zoomout():

    ret, img = cap.read()

    cv2.imshow('frame',img)



cap = cv2.VideoCapture(0)
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame',640,480)

count = 1

while(True):
    
    cv2.setMouseCallback('frame', mousecall)
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Orig.png', frame)
        print('Orig Save')

### PROGRAM ENDS HERE ####################

cap.release()
cv2.destroyAllWindows()