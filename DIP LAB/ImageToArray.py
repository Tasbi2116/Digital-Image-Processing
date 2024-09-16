# First Program: Read image and convert it to an array

import numpy as np
from PIL import Image

# Read the image using PIL
image = Image.open("D:/pixel.jpg")

# Convert the image to a NumPy array
image_array = np.array(image)

# Print the image array
print("Image Array:")
print(image_array)
print("  [ R   G   B ],......")
print(f"This image is:{image_array.shape[1]} X {image_array.shape[0]}")
# save the image array to a file
np.save('image_array.npy', image_array)
