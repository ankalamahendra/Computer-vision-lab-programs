import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
angle = 90
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.imwrite('rotated_image.jpg', rotated_image)
cv2.destroyAllWindows()
