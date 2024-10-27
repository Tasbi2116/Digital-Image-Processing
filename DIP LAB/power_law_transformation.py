
from PIL import Image
import numpy as nmpy

Image_original = Image.open("D:/bird.jpeg")
Gray_image = Image_original.convert('L')

Array = nmpy.array(Gray_image)
c = 1
gamma = 2

row, column = Array.shape
gamma_array = nmpy.zeros_like(Array, dtype=nmpy.float64)
# if we increase the gamma value the image will be darker
for i in range(row):
    for j in range(column):
        gamma_array[i,j] = (c*(Array[i,j]))**gamma

print("The Gamma Transform array = ", gamma_array)
a = (gamma_array - nmpy.min(gamma_array))
gamma_array = a/(nmpy.max(gamma_array) - nmpy.min(gamma_array))
gamma_array = gamma_array*255

gamma_array = gamma_array.astype(nmpy.uint8)
print("printing S:\n", gamma_array)
img = Image.fromarray(gamma_array)

img.show()