import base64
import requests
import wave
import soundfile


authentication = ('butter', 'fly')
page = requests.get('http://www.pythonchallenge.com/pc/hex/bin.html', auth= authentication)
contents = page.text
lines = str(contents)

email_code = lines[635:-39]

sound = open('indian.wav', 'wb')
data = base64.b64decode(email_code)
sound.write(data)
sound.close()

w = wave.open('indian.wav', 'rb')

indian = soundfile.SoundFile('indian.wav')

soundfile.write('result.wav', indian.read(), indian.samplerate, indian.subtype, 'BIG',indian.format)
