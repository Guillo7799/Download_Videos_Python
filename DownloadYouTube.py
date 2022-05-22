from base64 import urlsafe_b64decode
from pytube import YouTube
import os

path='path'
url=str(input('Ingrese Url: '))
print(str(url))
yt=YouTube(url)
print(yt.title)
try:
    #descargar con alta resolucion
    yt.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download(path)
    print("Descargado")
except:
    print("Error!")

response=str(input('¿Quiere descargar otro video? si/no: '))
while response == 'si':
    url=str(input('Ingrese Url: '))
    print(str(url))
    yt=YouTube(url)
    print(yt.title)
    try:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download(path)
        print("Descargado")
    except:
        print("Error!")
    response=str(input('¿Quiere descargar otro video? si/no: '))
else:
    print("Nos vemos :D")
    quit()



