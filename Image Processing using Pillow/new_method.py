from PIL import Image
# new method has three arguments 1. mode, 2. (height, weight), 3. color
# in RGB mode the color has three channel. Each channel has an intensity value from 0 to 255.
img = Image.new("RGB", (400,500), (0,0,255))
# img = Image.new("RGB", (400,500), "Yellow") this also possible.
img.show()