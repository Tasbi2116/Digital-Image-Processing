import cv2
import numpy as np

# Function to create a Gaussian kernel
def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma**2)) * np.exp(
            -((x - (size - 1) / 2)**2 + (y - (size - 1) / 2)**2) / (2 * sigma**2)
        ),
        (size, size),
    )
    return kernel / np.sum(kernel)

# Function to perform 2D convolution manually
def convolve(image, kernel):
    kernel_size = kernel.shape[0]
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)
    output = np.zeros_like(image, dtype=np.float32)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            output[i, j] = np.sum(region * kernel)

    return np.clip(output, 0, 255).astype(np.uint8)

# Read the input image as a grayscale image
image_path = 'D:\lion.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


kernel_size = 7
sigma = 1.0
kernel = gaussian_kernel(kernel_size, sigma)

# Apply Gaussian blur manually
blurred_image = convolve(original_image, kernel)

# High Boost Filter parameter (A > 1)
A = 2

# High Boost Filtering formula
high_boost_image = cv2.addWeighted(original_image, A, blurred_image, -1, 0)

cv2.imwrite('D:\high_bost_lion.jpg', high_boost_image)

cv2.imshow('Original Image', original_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('High Boost Filtered Image', high_boost_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("High Boost Filtering completed. Result saved as 'high_boost_result.png'.")