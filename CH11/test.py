from PIL import Image

cave = Image.open("cave.jfif")
cave_rgb = cave.convert("RGB")
pix = cave.load()
print(cave.size)  # Get the width and height of the image for iterating over

new_img = Image.new("RGB", (640,480))

for j in range (0,480, 2):
    for i in range(0, 640, 2):
        rgb_val_even = cave.getpixel((i,j ))
        rgb_val_odd= cave.getpixel((i+1,j+1))

        new_img.putpixel((i, j), rgb_val_even)
        new_img.putpixel((i, j), rgb_val_odd)


new_img.show()