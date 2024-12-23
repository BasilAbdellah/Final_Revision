import cv2
import numpy as np

image = np.ones((300,300,3),dtype=np.uint8)*255

cv2.rectangle(image,(100,100),(200,200),(0,255,0),-1)

scaled_img = cv2.resize(image,dsize=None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)

cv2.imshow('original',image)
cv2.imshow('scaled',scaled_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
