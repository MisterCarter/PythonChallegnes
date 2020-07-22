import requests


c_data = []
next_number = '12345'
while True:
    try:

        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=(next number)'
        url = url.replace('(next number)', next_number)
        page = requests.get(url)

        next_number = page.text.split()[-1]   # Splits starting from last element
        c_info = page.cookies['info']    #Gets cookies on url labelled info
        c_data.append(c_info)

        print(next_number, c_info)
    except:
        break
print(c_data)

x = ''.join(c_data)
print(x)

### decompressor = bz2.BZ2Decompressor()   creates an object!!
#### new_data = decompressor.decompress(data)