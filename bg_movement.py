import numpy as np
import cv2
#cap = cv2.VideoCapture('video.avi')
cap = cv2.VideoCapture('video.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
count = 0

while(1):
    count = count + 1
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame2',fgmask)
    image, contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(fgmask, contours, -1, (0,255,0), 3)

    cv2.imshow('frame',image)
    cv2.imwrite("frames/frame%d.jpg" % count, fgmask)

    # Program is exited upon pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()