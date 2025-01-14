import cv2
import numpy as np

input_image_path = r'D:\lion.jpg'  
image = cv2.imread(input_image_path)

if image is None:
    raise FileNotFoundError(f"Could not load image from {input_image_path}")

kernel = np.ones((3, 3), dtype=np.float32) / 9
height, width, channels = image.shape

pad = 1

# Initialize an empty matrix for the output 
blurred_image = np.zeros_like(image)

# Process each color channel independently
for c in range(channels):
    padded_channel = np.pad(image[:, :, c], ((pad, pad), (pad, pad)), mode='constant', constant_values=0)
    
    for i in range(height):
        for j in range(width):
            region = padded_channel[i:i+3, j:j+3]
            blurred_pixel = np.sum(region * kernel)
            blurred_image[i, j, c] = blurred_pixel

cv2.imshow("Input Image", image)
cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Input Image Array:")
print(image)

print("\nBlurred Image Array:")
print(blurred_image)