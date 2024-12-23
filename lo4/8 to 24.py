import cv2

image_gray = cv2.imread('small.jpg',cv2.IMREAD_GRAYSCALE)

RGB = cv2.cvtColor(image_gray,cv2.COLOR_GRAY2RGB)
RGB[:,:,1]=20
RGB[:,:,2]=50

display = cv2.cvtColor(RGB,cv2.COLOR_RGB2BGR)

cv2.imshow('gray',image_gray)
cv2.imshow('blue',display)

cv2.waitKey(0)
cv2.destroyAllWindows()