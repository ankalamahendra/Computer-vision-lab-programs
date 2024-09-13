import cv2
import numpy as np

image = cv2.imread("C:/Users/ankal/Downloads/butterfly.jpg")  
output_image = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

low_threshold = 50   
high_threshold = 150  
edges = cv2.Canny(blurred, low_threshold, high_threshold)


rho = 1              
theta = np.pi / 180  
threshold = 100       
min_line_length = 100 
max_line_gap = 10     

lines = cv2.HoughLinesP(edges, rho, theta, threshold, minLineLength=min_line_length, maxLineGap=max_line_gap)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Detected Lines', output_image)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
