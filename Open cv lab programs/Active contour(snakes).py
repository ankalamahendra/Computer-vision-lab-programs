import cv2
import numpy as np
from skimage import color, io
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import matplotlib.pyplot as plt

# Load the image
image_path = "C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg"
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image to remove noise
blurred_img = gaussian(gray, sigma=1)

# Display the grayscale and blurred images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Blurred Grayscale Image')
plt.imshow(blurred_img, cmap='gray')

# Initialize the snake contour (using a circle around the object)
s = np.linspace(0, 2 * np.pi, 400)
r = 100 + 100 * np.sin(s)  # y-coordinates
c = 150 + 100 * np.cos(s)  # x-coordinates
init = np.array([r, c]).T

# Perform active contour segmentation
snake = active_contour(blurred_img, init, alpha=0.015, beta=10, gamma=0.001)

# Create an image copy to draw the contour
contour_img = np.copy(img)

# Draw the snake contour on the original image
for coord in snake:
    x, y = int(coord[1]), int(coord[0])
    cv2.circle(contour_img, (x, y), 1, (0, 255, 0), -1)

# Display the contour-detected image
plt.subplot(1, 2, 2)
plt.title('Detected Contour')
plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))

plt.show()
