import cv2

# Load an image in BGR color space (default in OpenCV)
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/six-path-of-sasuke-and-naruto-laptop-drfo93pl8v6ou05k.webp")

# Convert the image to different color spaces
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the converted images
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('Lab Image', lab_image)
cv2.imshow('RGB Image', rgb_image)

# Wait indefinitely for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
