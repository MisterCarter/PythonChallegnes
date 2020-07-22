from PIL import Image, ImageDraw
from collections import Counter

# frame = Image.open('0.png')
#data = frame.load()

# width, height = frame.size
#
# print(width, height)
#
# pixel_lst = []    ## Creates a list with all pixel values. I then evaluate how many pixels of each colour there are
# for x in range(200):
#     for y in range(200):
#         z = frame.getpixel((x, y))
#         pixel_lst.append(z)
#
# print(pixel_lst)
# print(Counter(pixel_lst))  # Counter function used to count how many of each element in list
# print(pixel_lst.index(8))

#print(gif.n_frames)

# for frame in range(0,gif.n_frames):   CODE FOR SAVING MULTIPLE FILES WOHOO! FIRST PART FINDS EACH FRAME OF GIF
#                                      N_FRAMES IS THE MAX NUMBER OF FRAMES IN GIF
#
# gif.seek(frame)
# gif.save(str(frame)+'.png')
#
# for i in range(133): ##Opens all frames with gray pixels so that they can be changed to white
#     img = Image.open(str(i) + '.png')
#     data = img.load()
#     new_img = Image.new('L', frame.size)  # 'L' mode is for grayscale!! I create new images with new pixel data.
#     new_data = new_img.load()             # Could have edited same frames also.

#
#     for x in range(200): #Finds location of gray pixel in old frame and then puts a white one in the same location
#         for y in range(200):    # but in the new frames
#             if data[x, y] == 8:
#                 new_data[x, y] = 255
#     new_img.save('new'+ str(i) + '.png')
#
# import imageio
# import os
#
# folder = 'C:\pics'    ### Put images to be merged into a gif in this folder
# files = [f"{folder}\\{file}" for file in os.listdir(folder)]
#
# images = [imageio.imread(file) for file in files]
# imageio.mimwrite('movie.gif', images, fps=20)  # Creates gif with these settings in the same folder as script!!!!

img = Image.open('white.gif')
new_img = Image.new('L', (400,400))
data = new_img.load()
cursor_x, cursor_y = 100, 100
centre_x, centre_y = 100, 100
for frame_number in range(133):
    img.seek(frame_number)

    x , y, x2 , y2 = img.getbbox()
    x_diff = x - centre_x
    y_diff = y - centre_y

    if x_diff == 0 and y_diff == 0:
        cursor_x += 50

    cursor_x += x_diff
    cursor_y += y_diff
    data[cursor_x,cursor_y] = 255
    print('x',x, 'y', y)

new_img.show()