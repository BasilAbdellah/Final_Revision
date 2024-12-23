import cv2

BGR_image = cv2.imread('small.jpg')

# Convert the image to HSV
HSV = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2HSV)

hue_shift = int(input('enter : '))

HSV[:,:,0]=(HSV[:,:,0]+hue_shift) % 180

modified = cv2.cvtColor(HSV,cv2.COLOR_HSV2BGR)

cv2.imshow('modify',modified)
cv2.waitKey(0)
cv2.destroyAllWindows()