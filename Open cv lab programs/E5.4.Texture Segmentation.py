import cv2
import numpy as np
from sklearn.cluster import KMeans

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg", cv2.IMREAD_GRAYSCALE)

ksize = 21
sigma = 5.0
gamma = 0.5
lambd = 10.0
phi = 0
theta = np.pi / 4 
sigma_x = sigma
sigma_y = sigma / gamma
(x, y) = np.meshgrid(np.arange(ksize) - ksize // 2, np.arange(ksize) - ksize // 2)
x_theta = x * np.cos(theta) + y * np.sin(theta)
y_theta = -x * np.sin(theta) + y * np.cos(theta)
gabor_kernel = np.exp(-0.5 * (x_theta**2 / sigma_x**2 + y_theta**2 / sigma_y**2))
* np.cos(2 * np.pi / lambd * x_theta + phi)
filtered_image = cv2.filter2D(image, cv2.CV_32F, gabor_kernel)
features = filtered_image.flatten()
features = (features - np.mean(features)) / np.std(features)
features = features.reshape(-1, 1)
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters)
labels = kmeans.fit_predict(features)
segmented_image = labels.reshape(image.shape)
segmented_image = (segmented_image * (255 // (num_clusters - 1))).astype(np.uint8)
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
