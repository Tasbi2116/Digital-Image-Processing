from PIL import Image
img1 = Image.open("D:\same1.jpg")
img2 = Image.open("D:\same2.jpg")
img = Image.blend(img1, img2, alpha=0.8)
img.show()