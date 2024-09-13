import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg", cv2.IMREAD_GRAYSCALE)

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
canny_edges = cv2.Canny(blurred_image, 100, 200)  

sobel_x = cv2.Sobel(image, cv2.CV_16S, 1, 0)  
sobel_y = cv2.Sobel(image, cv2.CV_16S, 0, 1)  

abs_sobel_x = cv2.convertScaleAbs(sobel_x)
abs_sobel_y = cv2.convertScaleAbs(sobel_y)

sobel_edges = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

_, binary_sobel_edges = cv2.threshold(sobel_edges, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", canny_edges)
cv2.imshow("Sobel Edge Detection", binary_sobel_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
