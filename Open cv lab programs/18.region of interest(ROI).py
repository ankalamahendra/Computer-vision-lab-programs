import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
x, y, w, h = 50, 50, 200, 150  

roi = image[y:y+h, x:x+w]

# Process the ROI - Fill the ROI with a solid color (e.g., red)
# Define the color in BGR format
color = (0, 0, 255)  # Red color
image[y:y+h, x:x+w] = color

cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
