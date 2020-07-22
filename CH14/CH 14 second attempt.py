from PIL import Image

wire = Image.open('wire.png', 'r')
new_img = Image.new("RGB", (100,100))

x_min , x_max = 0 , 99
y_min , y_max = 0 , 99

position = [0, 0]
count = 0

while ( x_max-1 != x_min and y_max-1 != y_min ):
    print(x_max - 1)
    for x in range(x_min, x_max, 1):

        position[0] = x
        count += 1
        new_img.putpixel(position, wire.getpixel((count, 0)))

    y_min += 1

    for y in range (y_min, y_max, 1):

        position[1] = y
        count += 1
        new_img.putpixel(position, wire.getpixel((count, 0)))

    x_max -= 1

    for x in range(x_max, x_min, -1):

        position[0] = x
        count += 1
        new_img.putpixel(position, wire.getpixel((count, 0)))

    y_max -= 1

    for y in range(y_max, y_min, -1):

        position[1] = y
        count += 1
        new_img.putpixel(position, wire.getpixel((count, 0)))

    x_min += 1

new_img.show()
