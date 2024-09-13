import cv2

image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")
cv2.imshow('Image', image)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  
        break
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN: 
            print(f"Clicked coordinates: X={x}, Y={y}")
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, f"({x},{y})", (x, y), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.imshow('Image', image)

    cv2.setMouseCallback('Image', click_event)
cv2.destroyAllWindows()
