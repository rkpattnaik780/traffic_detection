import cv2
 
cap = cv2.VideoCapture('./video.avi')
 
car_cascade = cv2.CascadeClassifier('./cars.xml')
 
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
     
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    print ( "Cars count - " + str(len(cars)) )

    # Trigger some activity if no car is detected !! 

    if len(cars) == 0 : 
        pass

    cv2.imshow('video2', frames)
     
    # Program is exited upon pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cv2.destroyAllWindows()

