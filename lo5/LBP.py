import cv2
import numpy as np
from skimage.feature import local_binary_pattern
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

path = 'smakk.jpeg'

gray_image = cv2.imread(path,cv2.IMREAD_GRAYSCALE)

radius = 1
n_points = 8 * radius

lbp = local_binary_pattern(gray_image,n_points,radius,method='uniform')

lbp_hist , _ = np.histogram(lbp.ravel(),bins=np.arange(0,n_points+3))

lbp_hist = lbp_hist.astype(float)

lbp_hist /= (lbp_hist.sum() + 1e-6)


lbp_display = (lbp * (255 / lbp.max())).astype(np.uint8)

cv2.imshow('grey' , gray_image)
cv2.imshow('LBP' , lbp_display)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize=(8,6))
plt.bar(np.arange(0,len(lbp_hist)),lbp_hist,color='purple')
plt.title("LBP Histogram")
plt.xlabel("prototypes")
plt.ylabel("pixels")

plt.savefig("finish.png")