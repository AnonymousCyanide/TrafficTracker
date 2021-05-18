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
    # projects current image in media window named Frame
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)

    key = cv2.waitKey(0)
    # Progamr stops on esc
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()