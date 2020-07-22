from PIL import Image
source = Image.open('wire.png', 'r')

def spiral(source):
     target = Image.new(source.mode, (100, 100))
     left, top, right, bottom = (0, 0, 99, 99)
     x, y = 0, 0
     dirx, diry = 1, 0
     for i in range(10000):
         target.putpixel((x, y), source.getpixel((i, 0)))
         if dirx == 1 and x == right:
             dirx, diry = 0, 1
             top += 1
         elif dirx == -1 and x == left:
             dirx, diry = 0, -1
             bottom -= 1
         elif diry == 1 and y == bottom:
             dirx, diry = -1, 0
             right -= 1
         elif diry == -1 and y == top:
             dirx, diry = 1, 0
             left += 1
         x += dirx
         y += diry
     return target


x = spiral(source)

x.show()