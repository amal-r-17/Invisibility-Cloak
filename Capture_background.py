import cv2
cap = cv2.VideoCapture(0)

_, frame = cap.read()
while True:
    cv2.imshow("F",frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
cv2.imwrite("invisiblity.jpg",frame)

cap.release()