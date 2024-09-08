from PIL import Image
filename = "D:/pixel.jpg"
img = Image.open(filename)
print(img.width, img.height)
img.show()
img = img.resize((int(img.width/2), int(img.height/2)), resample= Image.LANCZOS, box=(10,10,100,100))
print(img.width, img.height)
img.show()