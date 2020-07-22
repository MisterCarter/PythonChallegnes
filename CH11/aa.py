from PIL import Image

cave = Image.open("cave.jfif")
cave_rgb = cave.convert("RGB")
pix = cave.load()
#print(cave.size)  # Get the width and height of the image for iterating over

new_img = Image.new("RGB", (640,480))

print (cave.getpixel((6,  6)))

