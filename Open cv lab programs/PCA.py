import cv2
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found or could not be loaded.")
    exit()

original_shape = image.shape
flattened_image = image.reshape(-1, original_shape[1])  

pca = PCA(n_components=50)  
data_pca = pca.fit_transform(flattened_image)
data_reconstructed = pca.inverse_transform(data_pca)
reconstructed_image = data_reconstructed.reshape(original_shape).astype(np.uint8)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Reconstructed Image")
plt.imshow(reconstructed_image, cmap='gray')

plt.show()
