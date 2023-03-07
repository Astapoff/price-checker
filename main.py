import os
import time

import pandas as pd
import requests
import statsmodels.api as sm
from dotenv import load_dotenv

load_dotenv()

# Настройки API биржи
ETHUSDT_URL = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
BTCUSDT_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
API_KEY = os.getenv('api_key')

# Задаем порог изменения цены за 60 минут (в процентах)
PRICE_CHANGE_THRESHOLD = 1


# Создаем функцию для вычисления движений ETHUSDT без влияния BTCUSDT
def calculate_eth_price(df):
    X = df["btc_price"]
    y = df["eth_price"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    eth_price_without_btc = model.predict([1, 0])[0]
    eth_price_with_btc = model.predict([1, df.iloc[-1]["btc_price"]])[0]
    eth_price_change = (eth_price_with_btc - eth_price_without_btc) / eth_price_without_btc * 100
    return eth_price_change


# Цикл для постоянного чтения данных и вычисления движений ETHUSDT
while True:
    # Получаем актуальные цены фьючерсов ETHUSDT и BTCUSDT с API
    headers = {"x-api-key": API_KEY}
    eth_response = requests.get(ETHUSDT_URL, headers=headers).json()
    btc_response = requests.get(BTCUSDT_URL, headers=headers).json()
    eth_price = eth_response["price"]
    btc_price = btc_response["price"]
    # Сохраняем цены в DataFrame для регрессионного анализа
    data = pd.DataFrame({
        "eth_price": [eth_price],
        "btc_price": [btc_price]
    })
    # Вычисляем изменение цены за последний час
    # и выводим сообщение в консоль при необходимости
    if len(data) >= 6:
        eth_price_change = calculate_eth_price(data)
        if abs(eth_price_change) >= PRICE_CHANGE_THRESHOLD:
            print(f"Цена ETHUSDT изменилась на {eth_price_change:.2f}% за последний час")
    # Ждем 10 секунд перед следующим запросом
    time.sleep(10)
