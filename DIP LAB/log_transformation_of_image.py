import cv2
import numpy as np

def log_transform_uint8(image):
    c = 255 / np.log(1 + np.max(image))  # Scaling constant
    
    # Apply the log transformation directly on the uint8 image
    log_image = c * np.log(1 + image)
    log_image = np.clip(log_image, 0, 255).astype(np.uint8)
    
    return log_image

image = cv2.imread("D:/bird.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not read the image.")
else:
    # Apply the log transformation without float conversion
    log_image_uint8 = log_transform_uint8(image)

    # Display the original and log-transformed images using OpenCV
    cv2.imshow("Original Image", image)
    cv2.imshow("Log Transformed Image", log_image_uint8)

    cv2.waitKey(0)
    cv2.destroyAllWindows()