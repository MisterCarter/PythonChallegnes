import requests



url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'

response_headers = {'Content-Type': 'image/jpeg', 'Content-Range': 'bytes 0-30202/2123456789', 'Transfer-Encoding': 'chunked', 'Date': 'Thu, 21 May 2020 17:17:29 GMT', 'Server': 'lighttpd/1.4.35'}
request_headers = {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}


response = requests.get(url, auth = ('butter', 'fly'), headers=request_headers)
print (response.request.headers)

end = 2123456789

x = response.headers['Content-Range']

next_piece = int(x.split('-')[1].split('/')[0])+1

# request_headers['Range'] = 'bytes=%i-%i' % (next_piece, end) OLD METHOD!!! USE METHODS BELOW
request_headers['Range'] = f'bytes={next_piece:d}-{end:d}'
request_headers['Range'] = 'bytes={:d}-{:d}'.format(next_piece, end)

response = requests.get(url, auth = ('butter', 'fly'), headers=request_headers)

print(response.text)

print(response.headers)


while True:
    try:
        response = requests.get(url, auth=('butter', 'fly'), headers=request_headers)
        #print(response.request.headers)

        end = 2123456789

        x = response.headers['Content-Range']

        next_piece = int(x.split('-')[1].split('/')[0]) + 1

        # request_headers['Range'] = 'bytes=%i-%i' % (next_piece, end) OLD METHOD!!! USE METHODS BELOW
        request_headers['Range'] = f'bytes={next_piece:d}-{end:d}'
        request_headers['Range'] = 'bytes={:d}-{:d}'.format(next_piece, end)

        response = requests.get(url, auth=('butter', 'fly'), headers=request_headers)

        print(response.text)

        print(response.headers['Content-Range'])
    except:
        break


next_piece = 2123456790
request_headers['Range'] = 'bytes={:d}-{:d}'.format(next_piece, end)
response = requests.get(url, auth=('butter', 'fly'), headers=request_headers)
print(response.text)
print(response.headers['Content-Range'])

string = 'esrever ni emankcin wen ruoy si drowssap eht'
print(string[::-1])


next_piece = 2123456743
request_headers['Range'] = 'bytes={:d}-{:d}'.format(next_piece, end)
response = requests.get(url, auth=('butter', 'fly'), headers=request_headers)
print(response.text)
print(response.headers['Content-Range'])

next_piece = 1152983631
request_headers['Range'] = 'bytes={:d}-{:d}'.format(next_piece, end)
response = requests.get(url, auth=('butter', 'fly'), headers=request_headers)
print(response.text)
print(response.headers['Content-Range'])


with open("level21.zip", "wb") as f:
    f.write(response.content)