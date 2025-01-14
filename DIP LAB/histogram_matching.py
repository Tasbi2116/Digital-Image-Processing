import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

import numpy as np
from PIL import Image as im, ImageDraw

# Load the target grayscale image for histogram matching
target_image = im.open("D:/grayScaleBird.png")
target_image.show()
target_image_array = np.array(target_image)
target_height, target_width = target_image_array.shape

# Initialize and calculate the histogram for the target image
target_histogram = np.zeros(256, dtype=int)
for row in range(target_height):
    for col in range(target_width):
        target_histogram[target_image_array[row, col]] += 1

# Create an image to represent the histogram of the target image
histogram_image_target = im.new('L', (256, 200), 255)
draw_target = ImageDraw.Draw(histogram_image_target)

max_hist_value_target = max(target_histogram)
scaled_histogram_target = (target_histogram / max_hist_value_target) * 200

for i in range(256):
    draw_target.line((i, 200, i, 200 - int(scaled_histogram_target[i])), fill=0)

histogram_image_target.show()

# Calculate the cumulative distribution function (CDF) for the target image
target_cdf = np.zeros(256, dtype=float)
target_cdf[0] = target_histogram[0]
for intensity in range(1, 256):
    target_cdf[intensity] = target_cdf[intensity - 1] + target_histogram[intensity]

# Normalize the target CDF to the range [0, 255]
target_cdf_normalized = 255 * (target_cdf / (target_height * target_width))
target_cdf_normalized = np.array(target_cdf_normalized, dtype=np.uint64)
print("Target CDF:", target_cdf_normalized)

# Load the source image to be matched to the target histogram
source_image = im.open('sampleGrey.jpg')
source_image.show()
source_image_array = np.array(source_image)
source_height, source_width = source_image_array.shape

# Initialize and calculate the histogram for the source image
source_histogram = np.zeros(256, dtype=int)
for row in range(source_height):
    for col in range(source_width):
        source_histogram[source_image_array[row, col]] += 1

# Create an image to represent the histogram of the source image
histogram_image_source = im.new('L', (256, 200), 255)
draw_source = ImageDraw.Draw(histogram_image_source)

max_hist_value_source = max(source_histogram)
scaled_histogram_source = (source_histogram / max_hist_value_source) * 200

for i in range(256):
    draw_source.line((i, 200, i, 200 - int(scaled_histogram_source[i])), fill=0)

histogram_image_source.show()

# Calculate the CDF for the source image
source_cdf = np.zeros(256, dtype=float)
source_cdf[0] = source_histogram[0]
for intensity in range(1, 256):
    source_cdf[intensity] = source_cdf[intensity - 1] + source_histogram[intensity]

# Normalize the source CDF to the range [0, 255]
source_cdf_normalized = 255 * (source_cdf / (source_height * source_width))
source_cdf_normalized = np.array(source_cdf_normalized, dtype=np.uint64)
print("Source CDF:", source_cdf_normalized)

# Perform histogram matching
matched_image_array = np.zeros_like(source_image_array)
matched_histogram = np.zeros(256, dtype=int)
mapping_values = []

# Find closest matching intensity for each source CDF value in the target CDF
for source_intensity in range(len(source_cdf_normalized)):
    min_difference = float('inf')
    closest_intensity = 0
    for target_intensity in range(len(target_cdf_normalized)):
        difference = abs(target_cdf_normalized[target_intensity] - source_cdf_normalized[source_intensity])
        if difference < min_difference:
            min_difference = difference
            closest_intensity = target_intensity
    mapping_values.append(closest_intensity)

# Apply the intensity mapping to create the matched image
for row in range(source_height):
    for col in range(source_width):
        matched_intensity = mapping_values[source_image_array[row, col]]
        matched_image_array[row, col] = matched_intensity
        matched_histogram[matched_intensity] += 1

# Create an image to represent the histogram of the matched image
histogram_image_matched = im.new('L', (256, 200), 255)
draw_matched = ImageDraw.Draw(histogram_image_matched)

max_hist_value_matched = max(matched_histogram)
scaled_histogram_matched = (matched_histogram / max_hist_value_matched) * 200

for i in range(256):
    draw_matched.line((i, 200, i, 200 - int(scaled_histogram_matched[i])), fill=0)

histogram_image_matched.show()

# Convert the matched array back to an image and display it
matched_image = im.fromarray(matched_image_array)
matched_image.show()