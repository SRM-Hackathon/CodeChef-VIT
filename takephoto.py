import cv2
cap=cv2.VideoCapture(0)
ret,photo=cap.read()
cv2.imshow("photo",photo)
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.imwrite("./images/src.jpg",photo)
cap.close()
