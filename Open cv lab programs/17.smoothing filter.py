import cv2
import numpy as np
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
kernel_size = 5

if kernel_size % 2 == 0:
    raise ValueError("Kernel size must be an odd integer.")

kernel = np.ones((kernel_size, kernel_size),
                 np.float32) / (kernel_size * kernel_size)
smoothed_image = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
