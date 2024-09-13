import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg",cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1)

cv2.imshow("Original image", image)
cv2.imshow("Erosion image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
