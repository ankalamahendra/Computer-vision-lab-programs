import cv2
import numpy as np
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray_image)
equ_bgr = cv2.cvtColor(equ, cv2.COLOR_GRAY2BGR)
result = np.hstack((image, equ_bgr))
cv2.imshow("Equalized image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

