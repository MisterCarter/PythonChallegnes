import hashlib

md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
data = open('mybroken.zip', 'rb').read()


def search_and_save():
    for i in range(len(data)):
        for j in range(256):
            new_data = (data[:i] + bytes([j]) + data[i + 1:])
            if hashlib.md5(new_data).hexdigest == md5code:
                open("repaired.zip", 'wb').write(new_data)
                return


md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
data = open('mybroken.zip', 'rb').read()
search_and_save()
