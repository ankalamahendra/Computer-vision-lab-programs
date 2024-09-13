import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg", cv2.IMREAD_GRAYSCALE)

# Threshold the image to create a binary image (black and white)
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Find the contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours and display their coordinates
for contour in contours:
    # Iterate over each point in the contour
    for point in contour:
        # Extract the x, y coordinates of each point in the contour
        x, y = point[0]
        print(f"Contour point coordinates: X={x}, Y={y}")
        # Draw a small circle at each contour point for visualization
        cv2.circle(image, (x, y), 3, (0, 0, 0), -1)

# Display the original image with contours marked
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
