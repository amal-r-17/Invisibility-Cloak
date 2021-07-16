# [106 111 109] - lower
# [184 255 255] - upper

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

base = cv2.imread("invisiblity.jpg")
base = cv2.flip(base,1)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([106,111,109])
    u_b = np.array([184,255,255])
    mask = cv2.inRange(hsv, l_b, u_b)
    #mask = cv2.bitwise_not(mask)

    cv2.imshow("Base", base)
    cv2.imshow("Mask", mask)
    #cv2.imshow("Final", res)
    frame[np.where(mask == 255)] = base[np.where(mask ==255)]
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
