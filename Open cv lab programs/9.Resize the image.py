import cv2
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
resized_image = cv2.resize(image, (1000, 800), interpolation=cv2.INTER_LINEAR)
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
