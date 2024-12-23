import cv2
import numpy as np

image =  cv2.imread('small.jpg')

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

value_adj = int(input('enter : '))

value_ch = hsv[:,:,2].astype(np.int32)
value_ch = np.clip(value_ch + value_adj,0,255).astype(np.uint8)
hsv[:,:,2] = value_ch

finish = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

cv2.imshow('original',image)
cv2.imshow('val',finish)

cv2.waitKey(0)
cv2.destroyAllWindows()