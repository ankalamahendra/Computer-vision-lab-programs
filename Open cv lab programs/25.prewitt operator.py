import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[-1, 0, 1], 
                     [-1, 0, 1], 
                     [-1, 0, 1]], dtype=np.float32)

kernel_y = np.array([[ 1,  1,  1], 
                     [ 0,  0,  0], 
                     [-1, -1, -1]], dtype=np.float32)
grad_x = cv2.filter2D(gray_image, -1, kernel_x)
grad_y = cv2.filter2D(gray_image, -1, kernel_y)

grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)

grad_magnitude = np.clip(grad_magnitude, 0, 255)
grad_magnitude = grad_magnitude.astype(np.uint8)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(grad_magnitude, cmap='gray')
plt.title('Prewitt Edge Detection')

plt.show()
