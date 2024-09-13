import cv2
from matplotlib import pyplot as plt
img = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
cv2.imshow("Original Image",img)
plt.hist(img.ravel(),256,[0,256])
plt.show()
