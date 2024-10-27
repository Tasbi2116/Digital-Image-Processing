import numpy as np
from PIL import Image

# Step 1: Read the color image using PIL
image = Image.open("D:/bird.jpeg")

# Convert the image to a NumPy array
image_array = np.array(image)


x1, y1 = 1000, 500  
x2, y2 = 2000, 1000  

box_array = image_array[y1:y2, x1:x2]

# Print the array values inside the box
print("Array values inside the box:")
print(box_array)

# Convert the box array back to an image using PIL
box_image = Image.fromarray(box_array)

# Show the cropped (boxed) image
box_image.show()

# Optionally, save the cropped image
box_image.save('cropped_box_image.jpeg')


solid_color = [255, 0, 0]  # Red color in RGB
image_array[y1:y2, x1:x2] = solid_color  


modified_image = Image.fromarray(image_array)


modified_image.show()

# Optionally, save the modified image with the filled box
modified_image.save('full_image_with_filled_box.jpeg')
