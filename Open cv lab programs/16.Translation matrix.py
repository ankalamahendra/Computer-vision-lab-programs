import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
height, width = image.shape[:2]

shift_x = 200 
shift_y = 100 

translation_matrix = np.float32([[1, 0, shift_x],
                                 [0, 1, shift_y]])
translated_image = cv2.warpAffine
(image,translation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
