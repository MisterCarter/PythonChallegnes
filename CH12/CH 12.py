
data = open("evil2.gfx", 'rb').read()
b = bytes([data[1]])
print (b)

images = {}
n = 5

for x in range(n):
    images[x] = open("image"+ str(x) + '.jpg', 'wb')

for y in range(0, len(data), 5):
    for x in range(n):
        images[x].write(bytes([data[y + x]]))





