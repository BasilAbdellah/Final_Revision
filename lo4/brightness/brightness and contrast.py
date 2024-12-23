import cv2

image  = cv2.imread('lol.jpg')

adjusted = cv2.convertScaleAbs(image,beta=50,alpha=1)
cv2.imwrite('edit.jpg',adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()