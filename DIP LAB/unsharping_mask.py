import numpy as np
from PIL import Image, ImageDraw, ImageFont

   
image_path = 'D:\\lion.jpg'  
original_image = Image.open(image_path).convert("L")  
original_array = np.array(original_image)

# Define a simple blur mask
mask = np.array([[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]) / 9 

# Perform convolution manually to blur the image
def convolve2d(image, mask):
    """
    Manually apply 2D convolution with the given mask.
    """
    mask_height, mask_width = mask.shape
    pad_h, pad_w = mask_height // 2, mask_width // 2

    # Pad the image with zeros
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    output = np.zeros_like(image)

    # Perform convolution
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + mask_height, j:j + mask_width]
            output[i, j] = np.sum(region * mask)

    return output

# convolution to blur the image
blurred_array = convolve2d(original_array, mask)

# calculate the mask (original - blurred)
mask_array = original_array - blurred_array
mask_array = np.clip(mask_array, 0, 255)  

# sharpened image by adding the mask to the original
sharpened_array = original_array + mask_array
sharpened_array = np.clip(sharpened_array, 0, 255) 

# Convert results back to images
blurred_image = Image.fromarray(blurred_array.astype(np.uint8))
mask_image = Image.fromarray(mask_array.astype(np.uint8))
sharpened_image = Image.fromarray(sharpened_array.astype(np.uint8))

# Function to add titles to images
def add_title(image, title, font_size=20):
    """
    Add a title to the image as text at the top.
    """
    # Create a new image with space for the title
    new_height = image.height + 50
    titled_image = Image.new("L", (image.width, new_height), color=255)  # White background
    titled_image.paste(image, (0, 50))

    # Draw the title on the image
    draw = ImageDraw.Draw(titled_image)
    font = ImageFont.load_default()

    # Calculate text size
    text_bbox = draw.textbbox((0, 0), title, font=font)  # Get bounding box of the text
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (image.width - text_width) // 2  # Center the title
    draw.text((text_x, 10), title, fill=0, font=font)

    return titled_image

original_with_title = add_title(original_image, "Original Image")
blurred_with_title = add_title(blurred_image, "Blurred Image")
mask_with_title = add_title(mask_image, "Mask (Original - Blurred)")
sharpened_with_title = add_title(sharpened_image, "Sharpened Image")

original_with_title.show()
blurred_with_title.show()
mask_with_title.show()
sharpened_with_title.show()