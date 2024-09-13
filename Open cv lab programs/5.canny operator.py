import cv2
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg", cv2.IMREAD_GRAYSCALE)


blurred_image = cv2.GaussianBlur(image, (5, 5), 1.5)
edges = cv2.Canny(blurred_image, 50, 150)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
