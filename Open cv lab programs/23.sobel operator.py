import cv2
imp ort numpy as np
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobelx, sobely)

sobel_combined = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX)
sobel_combined = np.uint8(sobel_combined)

cv2.imwrite('sobel_combined_final.jpg', sobel_combined)

cv2.imshow('Sobel Edge Detection', sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
