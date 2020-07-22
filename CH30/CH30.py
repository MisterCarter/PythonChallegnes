from PIL import Image
import math

with open('yankeedoodle.csv') as f: #Opens csv file and creates a list with all the csv items
    data = [x.strip() for x in f.read().split(",")]
    length = len(data)
print(length)
print(data)

#This is super random but Im supposed to find the prime factors of the length of the list formed by the csv file


z = 5 % 3
print(z)

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:            # % operator divides one number by another and returns the remainder of the division
           print(i)              #as an intger. No decimals so watch out!!!

print_factors(7367)

img = Image.new("F", (53, 139))
img.putdata([float(x) for x in data], 256)  #an offset of 0 returns a black image!! value of 256 is to make img legible


img = img.transpose(Image.FLIP_LEFT_RIGHT) # Mirrors it
img = img.transpose(Image.ROTATE_90)#Rotates 90 deegrees
#img.show()

# FORMULA FROM IMG: n = str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]

# x[i] = 0,3,6...     x[i+1] = 1,4,7...    x[i+2] = 2,5,8...
#Separate data accordingly

a = data[0::3]
b = data[1::3]
c = data[2::3]

res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])])


print(res)


test = data[0::3]
print(test)

# for x in bytes(zip(data[0::3], data[1::3], data[2::3]):
#     print(bytes(int(x[0][5] + x[1][5] + x[2][6])))

### WHY DOESNT THIS FUCKING WORK