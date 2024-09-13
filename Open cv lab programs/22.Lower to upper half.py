import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = gray_image.shape

if height % 2 != 0:
    gray_image = gray_image[:-1, :]
    height -= 1
lower_half = gray_image[height//2:, :]
mirrored_image = gray_image.copy()
mirrored_image[:height//2, :] = cv2.flip(lower_half, 0)  
cv2.imwrite('mirrored_image.jpg', mirrored_image)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Grayscale Image')
plt.imshow(gray_image, cmap='gray')

plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Mirrored Image')
plt.imshow(mirrored_image, cmap='gray')
plt.axis('off')

plt.show()
