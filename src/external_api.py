import os
from dotenv import load_dotenv
import requests
from typing import Any

load_dotenv('.env.example')  # загружаем переменные окружения из файла .env
API_KEY = os.getenv('ONi5gXqWWKPxDN3VJq8PHraO22pk9Ohu')

def conversion_transactions(transaction: dict) -> Any:
    """Функция принимает значение суммы в EUR и USD и конвертирует в рубли по акт курсу"""
    summ_transaction = float(transaction['operationAmount']['amount']) # конвертация суммы из словаря
    currency = transaction['operationAmount']['currency']['code'] # значение валюты

    my_headers = {"apikey": API_KEY}
    # Не доконца понял для чего эта строка
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={summ_transaction }"
    #URL согласно документации сайта,
    # to - в какую валюту
    # from - из какой валюты
    # from - сумма для конвертации
    responce = requests.get("GET", url, headers = my_headers) # вызов при помощи GET
    result = responce.json() # конвертация в json
    return float(round(result.get('result'),2))



