from PIL import Image
import numpy

wire = Image.open('wire.png')
#wire_rgb = wire.convert("RGB")
#pix = wire.load()
print(wire.size)
print(wire.size[0])

pixel_list = []

for i in range(wire.size[0]):
    x = wire.getpixel((i,0))
    pixel_list.append(x)
    print ('Pixel:'+ str(i+1), x)

print(pixel_list[0])

####100 accross, +99 down +99 back +98 up +98 accross +97 back +97 up and so on

new_img = Image.new("RGB", (100,100))
index = 0
d = 100
p = 0
q = 0

for p in range(d):
    new_img.putpixel((p,q) , pixel_list[p])
    for q in range (d-1):
        new_img.putpixel((d-1, 1), pixel_list[p+q])
        for r in range (d-1, 0, -1 ):
            new_img.putpixel((d - 1, 99), pixel_list[p + q + r])


new_img.show()