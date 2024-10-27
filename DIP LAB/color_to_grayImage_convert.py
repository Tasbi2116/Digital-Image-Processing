import numpy as np
from PIL import Image

# Read the color image using PIL
image = Image.open("D:/color_image.jpg")

# Convert the image to a NumPy array
image_array = np.array(image)

# Separate the image into Red, Green, and Blue channels
red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]


# Red: 30%, Green: 59%, Blue: 11%
gray_array = 0.3 * red_channel + 0.59 * green_channel + 0.11 * blue_channel

# Ensure the values are in the range [0, 255] and convert to uint8
gray_array = gray_array.astype(np.uint8)

# Convert the grayscale array back to an image
gray_image = Image.fromarray(gray_array)

# Show the grayscale image using PIL's .show() method
gray_image.show()

# Save the grayscale image if needed
gray_image.save('gray_image.jpeg')

# Save the grayscale array to a file
np.save('gray_image_array.npy', gray_array)
