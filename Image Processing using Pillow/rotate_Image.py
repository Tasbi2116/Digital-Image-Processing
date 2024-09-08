from PIL import Image
filename = "D:/pixel.jpg"
img = Image.open(filename)
img = img.rotate(angle=60, expand=True, fillcolor="white")
# there is one more parameter of rotate method that is resample = Image.BICUBIC used to have the high quality image after editing.
# center parameter change the rotation center of the image
img.show()