import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg") 

kernel = np.ones((5, 5), np.uint8)
tophat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Image', tophat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
