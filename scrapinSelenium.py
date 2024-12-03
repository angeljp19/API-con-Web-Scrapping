from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.currencyPair


options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
    

urls = [
    'https://es.tradingview.com/symbols/EURUSD/?exchange=OANDA',
    'https://es.tradingview.com/symbols/EURJPY/?exchange=OANDA',
    'https://es.tradingview.com/symbols/EURGBP/?exchange=OANDA',
    'https://es.tradingview.com/symbols/USDJPY/?exchange=OANDA',
    'https://es.tradingview.com/symbols/GBPUSD/?exchange=OANDA',
    'https://es.tradingview.com/symbols/AUDUSD/?exchange=OANDA',
    'https://es.tradingview.com/symbols/AUDJPY/?exchange=OANDA',
    'https://es.tradingview.com/symbols/AUDCAD/?exchange=OANDA',
    'https://es.tradingview.com/symbols/GBPJPY/?exchange=OANDA',
    'https://es.tradingview.com/symbols/USDCHF/?exchange=OANDA',
    'https://es.tradingview.com/symbols/NZDUSD/?exchange=OANDA',
    'https://es.tradingview.com/symbols/CADCHF/?exchange=OANDA',
    'https://es.tradingview.com/symbols/USDCAD/?exchange=OANDA',
]

def scrape(url):
    driver.get(url)

    sleep(5)

    price = driver.find_element(By.CLASS_NAME, 'lastContainer-JWoJqCpY')
    symbol = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[2]/button[2]/span[1]/span[1]/div/span[1]')
    change = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[2]')
    name = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/h1')
    volumen = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[2]/div/section/div[3]/div[2]/div/div[1]/div[2]/div[1]/div')
    rangoDelDia = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[2]/div/section/div[3]/div[2]/div/div[4]/div[2]/div[1]/div/div')

    change_text = change.text

    if "\u2212" in change_text:
        change_text = change_text.replace("\u2212", "-")
    change_text = change_text.replace("\n", " ")
    data = {"price": price.text, "symbol": symbol.text, "change": change_text, "name": name.text, "volumen": volumen.text, "rangoDelDia": rangoDelDia.text}
    
    pair = db[symbol.text]
    pair.insert_one(data)

    print(data)


while True:
    for url in urls:
        scrape(url)
        

