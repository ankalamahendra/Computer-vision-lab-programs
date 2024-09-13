import cv2
image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg")
blur_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Gaussian Blurred Image', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
