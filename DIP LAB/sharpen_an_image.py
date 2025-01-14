import cv2
import numpy as np

image = cv2.imread('D:\lion.jpg')

# Define the sharpening mask
mask = np.array([[0, -1, 0],
                 [-1, 5, -1],
                 [0, -1, 0]])

# Apply the sharpening filter using cv2.filter2D
sharpened_image = cv2.filter2D(image, -1, mask)

cv2.imshow("Original Image", image)            
cv2.imshow("Sharpened Image", sharpened_image)  

print("Original Image Array:")
print(image) 

print("\nSharpened Image Array:")
print(sharpened_image) 

cv2.waitKey(0)
cv2.destroyAllWindows()