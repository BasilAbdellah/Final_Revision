import cv2

image  = cv2.imread('lol.jpg')

new = cv2.resize(image,dsize=None,fx=0.2,fy=0.2)

cv2.imwrite('small.jpg',new)

cv2.waitKey(0)
cv2.destroyAllWindows()