from PIL import Image
from collections import Counter

maze = Image.open('maze.png')
data = maze.load()

pxl_lst = []

for x in range(641):
    for y in range(641):
        z = maze.getpixel((x, y))
        pxl_lst.append(z)
        print('Coordinates:', x, ',', y, 'Colour Value:', z)

print(Counter(pxl_lst))

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]     # y+, y-, x+, x-
white = (255, 255, 255, 255)
entrance = (639, 0)
exit = (1, 640)

queue = [exit] #Pixels left to visit

visited = [] #Pixels visited

