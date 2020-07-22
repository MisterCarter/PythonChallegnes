import requests




url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
#url = url.replace('(next number)', next_number)
data = {'info': 'the flowers are on their way'}
page = requests.get(url, cookies=data)
print (page.text)


