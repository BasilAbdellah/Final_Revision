import cv2

image  = cv2.imread("lol.jpg")

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("grey",gray_image)
cv2.imshow('original',image)
cv2.imwrite('edited.jpg',gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()