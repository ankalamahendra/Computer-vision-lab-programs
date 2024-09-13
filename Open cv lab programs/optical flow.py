import cv2
import numpy as np

# Load a sequence of images (example: img1.jpg, img2.jpg, etc.)
# Adjust the path and filenames according to your actual images.
image_folder = "C:/Users/ankal/OneDrive/Desktop/naruto"
total_frames = 5  # Number of images in the sequence

image_sequence = []
for i in range(1, total_frames + 1):
    img = cv2.imread(f"{image_folder}/img{i}.jpg")
    if img is None:
        print(f"Image {i} not found")
        continue
    image_sequence.append(img)

# Ensure that we have at least two images to calculate optical flow
if len(image_sequence) < 2:
    print("Not enough images to compute optical flow")
    exit()

# Convert the first image to grayscale
prev_img = cv2.cvtColor(image_sequence[0], cv2.COLOR_BGR2GRAY)

# Process each consecutive pair of images
for i in range(1, len(image_sequence)):
    next_img = cv2.cvtColor(image_sequence[i], cv2.COLOR_BGR2GRAY)

    # Compute dense optical flow using Farneback's method
    flow = cv2.calcOpticalFlowFarneback(prev_img, next_img, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Create an RGB image to visualize the flow
    h, w = prev_img.shape
    flow_visual = np.zeros((h, w, 3), dtype=np.uint8)

    # Normalize flow vectors for visualization
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    flow_visual[..., 0] = ang * 180 / np.pi / 2  # Angle of motion (H)
    flow_visual[..., 1] = 255  # Saturation (constant)
    flow_visual[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)  # Magnitude (V)

    # Convert HSV image to BGR for display
    flow_visual_bgr = cv2.cvtColor(flow_visual, cv2.COLOR_HSV2BGR)

    # Show the original image and the motion visualization
    cv2.imshow("Original Image", image_sequence[i])
    cv2.imshow("Optical Flow Visualization", flow_visual_bgr)

    # Wait for a short interval to create an animation effect
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # Set the next image as the previous one for the next loop
    prev_img = next_img

cv2.destroyAllWindows()
