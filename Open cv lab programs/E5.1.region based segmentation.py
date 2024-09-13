import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg", cv2.IMREAD_GRAYSCALE)

height, width = image.shape

seed_point = (100, 150) 
threshold = 10

segmented_image = np.zeros_like(image)

stack = [seed_point]
seed_value = image[seed_point[1], seed_point[0]]  

visited = np.zeros_like(image, dtype=bool)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while stack:
    x, y = stack.pop()  
    if visited[y, x]:
        continue  

    visited[y, x] = True
    
    if abs(int(image[y, x]) - int(seed_value)) <= threshold:
        segmented_image[y, x] = 255  

        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]

            if 0 <= nx < width and 0 <= ny < height and not visited[ny, nx]:
                stack.append((nx, ny))

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
