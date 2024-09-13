import cv2
cap = cv2.VideoCapture("C:/Users/ankal/Videos/Screen Recordings/Screen Recording 2024-09-04 143540.mp4")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        break
    cv2.imshow('Video Frame', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
