import cv2
import numpy as np

img = np.ones((400,400,3) , dtype = np.uint8) * 255

cv2.rectangle(img,(100,100),(300,300),(0,255,0),2)

# cv2.line(img,(50,50),(350,350),(255,0,0),2)
# cv2.line(img,(150,50),(150,350),(0,0,255),2)


x_min , y_min = 100 , 100
x_max , y_max = 300 , 300


# blue line
x1 ,y1 = 50,50
x2 , y2 = 350 ,350

if x1 < x_min : x1 = x_min
if x2 > x_max : x2 = x_max
if y1 < y_min : y1 = y_min
if y2 > y_max : y2 = y_max
cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

# red line
x1 ,y1 = 150,50
x2 , y2 = 150 ,350

if x1 < x_min : x1 = x_min
if x2 > x_max : x2 = x_max
if y1 < y_min : y1 = y_min
if y2 > y_max : y2 = y_max
cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)



cv2.imshow('clipped',img)

cv2.waitKey(0)
cv2.destroyAllWindows()