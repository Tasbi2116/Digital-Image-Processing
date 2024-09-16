# Second Program: Convert array back to an image and display it

import numpy as np
from PIL import Image

# Load the image array (from the .npy file)
image_array = np.load('image_array.npy')

# Convert the NumPy array back to an image
image = Image.fromarray(image_array)

# Show the image
image.show()
