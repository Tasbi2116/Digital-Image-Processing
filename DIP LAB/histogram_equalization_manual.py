import numpy as np
from PIL import Image, ImageDraw

# Load the grayscale image
original_image = Image.open("D:/grayScaleBird.png")
original_image.show()

# Convert image to a NumPy array
image_array = np.array(original_image)
image_height, image_width = image_array.shape

# Initialize histogram array for intensity values (0-255)
intensity_histogram = np.zeros(256, dtype=int)

# Calculate the histogram of the original image
for row in range(image_height):
    for col in range(image_width):
        intensity_histogram[image_array[row, col]] += 1

# Create an image to represent the histogram of the original image
histogram_image = Image.new('L', (256, 200), 255)
draw = ImageDraw.Draw(histogram_image)

# Scale the histogram values for visualization
max_hist_value = max(intensity_histogram)
scaled_histogram = (intensity_histogram / max_hist_value) * 200

for i in range(256):
    draw.line((i, 200, i, 200 - int(scaled_histogram[i])), fill=0)

histogram_image.show()

# Compute cumulative distribution function (CDF) for histogram equalization
cdf_array = np.zeros(256, dtype=float)
cdf_array[0] = intensity_histogram[0]

for intensity in range(1, 256):
    cdf_array[intensity] = cdf_array[intensity - 1] + intensity_histogram[intensity]

# Normalize the CDF values to map them to intensity range [0, 255]
cdf_normalized = 255 * (cdf_array / (image_height * image_width))

# Create an image to represent the normalized CDF
cdf_image = Image.new('L', (256, 200), 255)
draw = ImageDraw.Draw(cdf_image)

# Scale the CDF values for visualization
for i in range(256):
    draw.line((i, 200, i, 200 - int((cdf_normalized[i] / 255) * 200)), fill=0)

cdf_image.show()

# Convert normalized CDF to integer values
cdf_normalized = np.array(cdf_normalized, dtype=np.uint8)

# Create the equalized image array
equalized_image_array = np.zeros_like(image_array, dtype=np.uint8)
equalized_histogram = np.zeros(256, dtype=int)

# Apply the histogram equalization
for row in range(image_height):
    for col in range(image_width):
        equalized_intensity = cdf_normalized[image_array[row, col]]
        equalized_image_array[row, col] = equalized_intensity
        equalized_histogram[equalized_intensity] += 1

# Create an image to represent the histogram of the equalized image
equalized_histogram_image = Image.new('L', (256, 200), 255)
draw = ImageDraw.Draw(equalized_histogram_image)

# Scale the equalized histogram values for visualization
max_equalized_hist_value = max(equalized_histogram)
scaled_equalized_histogram = (equalized_histogram / max_equalized_hist_value) * 200

for i in range(256):
    draw.line((i, 200, i, 200 - int(scaled_equalized_histogram[i])), fill=0)

equalized_histogram_image.show()

# Convert the equalized array back to an image and display it
equalized_image = Image.fromarray(equalized_image_array)
equalized_image.show()