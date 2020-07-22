import zlib, bz2, magic

with open("package.pack", "rb") as f:
    data = f.read()

print(data)

x = magic.from_file('package.pack')  ## HOW TO CHECK THE FILE TYPE ##
print(x)

result = ''
with open("package.pack", "rb") as f:
    data = f.read()

    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith(b'BZh'):
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
            result += '\n'

        else:
            break
    print(result)
print(data[::-1]) #REMEMBER THIS REVERSES THE ORDER OF ARRAY VERY USEFUL

