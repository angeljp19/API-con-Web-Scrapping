## Web Scrapping
__Tecnologias y herramientes utilizadas:__
  -  Python
  -  Flask
  -  Selenium
  -  Mongodb

Este app utiliza Selenium para escrapear datos de pares de divisa en TradingView. De manera repetitiva cada 5 segundos carga las direcciones en la lista de 'urls', donde extrae los datos:
  -  Nombre
  -  Simbolo
  -  Precio
  -  Cambio
  -  Volumen
  -  Rango del dia

Luego de crear un arreglo con todos los datos los inserta en una base de datos de MongoDB, de manera organizada cada registro es guardado en su coleccion correspondiente

## API
Con el archivo 'main.py' se ejecuta un servidor de flask para habilitar la API que servira los datos del par de divisa solicitado que debe especificarse de la siguiente manera:

```
127.0.0.1:5000/price?symbol=USDJPY
```
El argumento symbol corresponder al simbolo del par de divisa que quiera solicitarse.

>[!WARNING] 
Cualquier cambio realizado en las paginas de TradingView puede afectar el funcionamiento de esta app, al igual que la version de este ChromeDriver y la version de Chrome que tengas en tu computadora.
