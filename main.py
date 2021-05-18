import cv2
# stores all video frame in cap
cap = cv2.VideoCapture('highway.mp4')

# Detect vehicals 
# checks for moving objects in this context vehicals
vehical_detector = cv2.createBackgroundSubtractorMOG2()


while True:
    # stores current frame in frame
    ret , frame  = cap.read()
    # Marks moving vehicals as white
    mask = vehical_detector.apply(frame)
    # vehical detection
    contours , _ = cv2.findContours(mask , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # Calculate are
        area = cv2.contourArea(cnt)
        if area>100:
         cv2.drawContours(frame , [cnt] , -1,(0 ,0 ,255), 1)
        

    # projects current image in media window named Frame
    cv2.imshow('Frame',frame)
    #cv2.imshow('Mask',mask)

    key = cv2.waitKey(60)
    # Progamr stops on esc
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()