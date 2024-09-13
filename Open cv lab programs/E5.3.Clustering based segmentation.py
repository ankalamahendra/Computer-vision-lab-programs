import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pixels = image_rgb.reshape((-1, 3))
pixels = np.float32(pixels)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3  
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]

segmented_image = segmented_image.reshape(image.shape)

cv2.imshow("Original Image", image)
cv2.imshow("K-means Segmentation", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
