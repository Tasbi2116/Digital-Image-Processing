from PIL import Image
filename = "D:/pixel.jpg"
img = Image.open(filename)
imgCropped = img.crop(box = (20,20,200,200))
print(imgCropped.width, imgCropped.height)
imgCropped.show()