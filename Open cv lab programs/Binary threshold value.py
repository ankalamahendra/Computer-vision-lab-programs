import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg", cv2.IMREAD_GRAYSCALE)

threshold_value = 127  
max_value = 255 

_, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Binary Threshold Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
