from PIL import Image

mozart = Image.open('Mozart.gif')  # 640 x 480   (Find 5 pixels with value 195, then remember there are 2 white ones
                                   #               on each side)

x = 0
y = 0


for y in range(479):
    for x in range(636):
        mozart.getpixel((x, y))
        if (mozart.getpixel((x, y)) == mozart.getpixel((x + 1, y)) == mozart.getpixel((x + 2, y)) == mozart.getpixel((x + 3, y)) == mozart.getpixel((x + 4, y)) == 195):

            mozart_cropped_1 = mozart.crop((x - 1, y, 640, y + 1))
            mozart_cropped_2 = mozart.crop((0, y, x - 1, y + 1))

            mozart.paste(mozart_cropped_1,  (0,y))
            mozart.paste(mozart_cropped_2, (x - 1, y))
mozart.show()