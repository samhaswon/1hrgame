import rembg
from PIL import Image

img = Image.open("./1616515264896.jfif")

result = rembg.remove(img)

result.save("./sprite.png")