import gzip
import difflib

f=gzip.open('deltas.gz','rb')
file_content = f.read().splitlines()
print (file_content)

left, right = [],[]

for line in file_content:
    left.append(line[:53])
    right.append(line[56:])

d = list(difflib.Differ().compare(left, right))

png = ['','','']

for row in d:
    print (row)
    for element in row:
        stuff = row[2:].split()

    if row[0] == '+':
        png[0] += ''.join(stuff)

    if row[0] == '-':
        png[1] += ''.join(stuff)

    if row[0] == ' ':
        png[2] += ''.join(stuff)

arr = bytes(png[0], 'utf-8')
print(arr)

open('18_%d.png' % 0,'wb').write(png[0])