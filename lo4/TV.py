import cv2

from skimage.restoration import denoise_tv_chambolle

image = cv2.imread('small.jpg',cv2.IMREAD_GRAYSCALE)

tv = denoise_tv_chambolle(image,weight=0.9)

cv2.imshow('original',image)
cv2.imshow('tv',tv)

cv2.waitKey(0)
cv2.destroyAllWindows()