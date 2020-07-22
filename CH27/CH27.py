from PIL import Image
import bz2
gif = Image.open("static.gif",'r')

#print(gif.size)

for x in range(320):
    for y in range(270):
        pxl_color = gif.getpixel((x,y))
        #print('(', x, y, ')', pxl_color)


palette = gif.getpalette()[::3] #[(x,x,x), (y,y,y)......] THese are RGB Values!!!
#print(palette)
#print(palette[::3]) #Eliminating triplicates from list
p = palette[::3]

table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))

raw = gif.tobytes()

trans = raw.translate(table)

#print(raw)
#print(table)
#print (trans)
# x = bytes(i for i in range(256))
# print (x)

zipped = list(zip(raw[1:], trans[:-1]))
print ('z',zipped)
print(len(zipped))

diff = list(filter(lambda p: p[0] != p[1], zipped)) ## Lambda function for p: in zipped, it filters out items following
#condition: p[0] != p[1] Extracts items (tuple) in list that have subitems unequal to each other.

print (diff)
#print(len(diff))

indices = [i for i,p in enumerate(zipped) if p[0] != p[1]]

print(diff[113])

print(zipped[113])
print(indices)

im2 = Image.new("RGB", gif.size)
colors = [(255, 255, 255)] * len(raw)
for i in indices:
    colors[i] = (0, 0, 0)
im2.putdata(colors)
im2.show()

s = [t[0] for t in diff]  ####Returns first subitem from each item in the list: diff
text = bz2.decompress(bytes(s))

print('s',s)
print(len(s))
print(len(indices))

import keyword
print(set([w for w in text.split() if not keyword.iskeyword(w.decode())]))

###### CHECK STUFF AGAIN IN DETAIL LOTS TO LEARN!!!!!