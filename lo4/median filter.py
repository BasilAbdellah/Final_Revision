import cv2

image = cv2.imread("OIP (1).jpg")

filter = cv2.medianBlur(image,5)

cv2.imshow("original",image)
cv2.imshow("filter",filter)

cv2.waitKey(0)
cv2.destroyAllWindows()