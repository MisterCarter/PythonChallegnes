from PIL import Image

mozart = Image.open('Mozart.gif')  # 640 x 480   (Find 5 pixels with value 195, then remember there are 2 white ones
                                   #               on each side)

x=429
y=0

mozart_cropped_1 = mozart.crop((x - 1, y, 640, y + 1))
mozart_cropped_2 = mozart.crop((0, y, x - 1, y + 1))

mozart.paste(mozart_cropped_1, (0,y))
mozart.paste(mozart_cropped_2, (x - 1, y))

mozart.show()
