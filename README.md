# 📊 API TradingView Scraper

> API RESTful desarrollada en **Python** que obtiene y sirve información actualizada de pares de divisas mediante **Web Scraping** de TradingView.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey?logo=flask)
![Selenium](https://img.shields.io/badge/Selenium-WebScraping-brightgreen?logo=selenium)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?logo=mongodb)

---

## 🚀 Descripción

Esta API permite consultar en tiempo real datos de pares de divisas extraídos directamente desde [TradingView](https://www.tradingview.com/).  
Automatiza la recolección de información financiera y la expone a través de un servidor **Flask**.

**Características principales:**
- Scraping automatizado con **Selenium** y **ChromeDriver**.
- Almacenamiento en **MongoDB** para consultas rápidas.
- API REST que devuelve información en formato JSON.
- Consultas dinámicas por símbolo de par de divisas.

---

## 🛠 Tecnologías utilizadas
- **Python**
- **Flask** — servidor API
- **Selenium** — scraping de datos
- **ChromeDriver** — automatización de navegador
- **MongoDB** — almacenamiento de datos

---

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
