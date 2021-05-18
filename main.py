import cv2
# stores all video frame in cap
cap = cv2.VideoCapture('highway.mp4')

while True:
    # stores current frame in frame
    ret , frame  = cap.read()
    # projects current image in media window named Frame
    cv2.imshow('Frame',frame)

    key = cv2.waitKey(0)
    # Progamr stops on esc
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()