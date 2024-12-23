import cv2
import numpy as np
image = cv2.imread('small.jpg')

hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)

saturation = hsv[:,:,1]

multiplier = float(input("enter : "))

saturation = np.clip(saturation * multiplier , 0 , 255)

hsv[:,:,1] = saturation

finish = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

cv2.imshow('original',image)
cv2.imshow('sat',finish)

cv2.waitKey(0)
cv2.destroyAllWindows()