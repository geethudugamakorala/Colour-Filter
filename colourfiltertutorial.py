#import required libraries
import cv2
import numpy as np

#strat capturing video and configure
video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

#define upper and lower HSV range for filtering colours
#change this range to filter different colours
filterLower = np.array([94, 80, 2], np.uint8)
filterUpper = np.array([126, 255, 255], np.uint8)

#start while loop to make it video
while True:
    #frame is like a single image,capture single image for that instant
    ret, frame = video.read()

    #Video from web camera is at BGR colour range
    # convert frame BGR range to HSV range of colours
    # in HSV range it is easier to identify colours
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Filter the range of colours we set earlier
    Filter = cv2.inRange(hsvFrame, filterLower, filterUpper)

    #get the actual colour filtered
    filterColour = cv2.bitwise_and(frame, frame, mask= Filter)

    #Show all changes in different windows
    cv2.imshow("Original", frame)
    cv2.imshow("HSVConverted", hsvFrame)
    cv2.imshow("Filter", Filter)
    cv2.imshow("Coloured filter", filterColour)

    key = cv2.waitKey(1)  # how long window displayed
    if key == ord('q'):  # breaking the while loop if q is presssed
        break

video.release()
cv2.destroyAllWindows()


