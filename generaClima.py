import requests

key= "feb7f94192f44091b4100d55e418590d"
url = 'https://api.openweathermap.org/data/2.5/weather?id=524901&lang=es&appid='+key
respuesta = requests.get(url)
contenido = respuesta.content
archivo =open('clima.json','wb')
archivo.write(contenido)
archivo.close
