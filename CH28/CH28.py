from PIL import Image

im = Image.open('bell.png')

# split RGB and get Green
green = list(im.split()[1].getdata()) ###Splits into three bands and creates image of each one
                                      # (one for RED, one for GREEN...) Thats why I choose [1] as i want green image
print(green)

# calculate diff for every two bytes by creating list with evens and odds. It then subtracts odd from even for each item
diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]
g1 = green[0::2]
g2 = green[1::2]



C = []
for i in range(len(g1)):
    difference = abs(g1[i] - g2[i])
    C.append(difference)
print(C)  #EQUIVALENT TO METHOD ABOVE!!! IT SUBTRACTS ONE LIST FROM ANOTHER AND TAKES ABSOLUTE VALUE

# remove the most frequent value 42
filtered = list(filter(lambda x: x != 42, diff))
print(filtered)
# convert to string and print out
print(bytes(filtered).decode())

lst= [1,2,3,4,5,6,7,8,9]

print(lst[0::2])
print(lst[1::2])