import os
from dotenv import load_dotenv
import requests
from typing import Dict

# load_dotenv('.env')  # почему то в этом случае не работает
load_dotenv()  # Загружаем переменные окружения
API_KEY = os.getenv('API_KEY')  # Ключ API из .env


def conversion_transactions(transaction: Dict) -> float:
    """Функция принимает значение суммы в EUR и USD и конвертирует в рубли по акт курсу"""
    amount = float(transaction['operationAmount']['amount'])  # Извлекаем сумму
    currency = transaction['operationAmount']['currency']['code']  # Извлекаем валюту

    headers = {"apikey": API_KEY}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    # URL согласно документации сайта,
    # to - в какую валюту
    # from - из какой валюты
    # amount - сумма для конвертации
    response = requests.get(url, headers=headers)  # вызов при помощи GET

    if response.status_code != 200:
        raise Exception(f"Ошибка API: {response.status_code}. Ответ: {response.text}")

    result = response.json()  # конвертация в json
    return round(float(result.get('result')), 2)

# if __name__ == '__main__':
#     data = {"operationAmount": {"amount": "8221.37","currency": {"code": "RUB"}}}
#
#     print(conversion_transactions(data))
