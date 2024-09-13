import cv2
import numpy as np

def nothing(x):
    pass
image = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('BGR Color Palette')
cv2.createTrackbar('Blue', 'BGR Color Palette', 0, 255, nothing)
cv2.createTrackbar('Green', 'BGR Color Palette', 0, 255, nothing)
cv2.createTrackbar('Red', 'BGR Color Palette', 0, 255, nothing)

while True:
    blue = cv2.getTrackbarPos('Blue', 'BGR Color Palette')
    green = cv2.getTrackbarPos('Green', 'BGR Color Palette')
    red = cv2.getTrackbarPos('Red', 'BGR Color Palette')

    image[:] = [blue, green, red]
    cv2.imshow('BGR Color Palette', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
