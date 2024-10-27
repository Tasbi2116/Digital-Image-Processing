import numpy as np
from PIL import Image

# Read the image using PIL
image = Image.open("D:/color_image.jpg")

# Convert the image to a NumPy array
image_array = np.array(image)
negative_image_array = 255 - image_array

negative_image = Image.fromarray(negative_image_array)
# Print the image array
print("Image Array:")
print(image_array)
print("  [ R   G   B ],......")
print(f"This image is:{image_array.shape[1]} X {image_array.shape[0]}") 
negative_image.show()
