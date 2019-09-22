import cv2
import nothing
import numpy as np

capture = cv2.VideoCapture(0)

cv2.namedWindow("HSV Tracking")

cv2.createTrackbar("Lower Hue", "HSV Tracking", 0, 255, nothing.do)
cv2.createTrackbar("Upper Hue", "HSV Tracking", 255, 255, nothing.do)
cv2.createTrackbar("Lower Saturation", "HSV Tracking", 0, 255, nothing.do)
cv2.createTrackbar("Upper Saturation", "HSV Tracking", 255, 255, nothing.do)
cv2.createTrackbar("Lower Value", "HSV Tracking", 0, 255, nothing.do)
cv2.createTrackbar("Upper Value", "HSV Tracking", 255, 255, nothing.do)

while (True):

    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hue = cv2.getTrackbarPos("Lower Hue", "HSV Tracking")
    upper_hue = cv2.getTrackbarPos("Upper Hue", "HSV Tracking")

    lower_saturation = cv2.getTrackbarPos("Lower Saturation", "HSV Tracking")
    upper_saturation = cv2.getTrackbarPos("Upper Saturation", "HSV Tracking")

    lower_value = cv2.getTrackbarPos("Lower Value", "HSV Tracking")
    upper_value = cv2.getTrackbarPos("Upper Value", "HSV Tracking")

    lower_hsv = np.array([[lower_hue, lower_saturation, lower_value]])
    upper_hsv = np.array([[upper_hue, upper_saturation, upper_value]])

    mask = cv2.inRange(src=hsv, lowerb=lower_hsv, upperb=upper_hsv)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('video', result)
    # cv2.imshow('video', frame)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
