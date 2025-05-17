import json
import os
import logging
# from src.external_api import conversion_transactions
from src import external_api

logger = logging.getLogger('utils')  # Создаем логгер с именем 'masks'
logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования INFO
file_handler = logging.FileHandler('logs/utils.log', encoding="utf-8")  # Создаем обработчик для записи логов в файл
# Настраиваем формат записей в логе
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
file_handler.setFormatter(file_formatter)  # Применяем форматтер к обработчику
logger.addHandler(file_handler)  # Добавляем обработчик к логгеру





# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_TO_FILE = os.path.join(BASE_DIR, "data", "operations.json")


def check_transactions_json(operations_json: str) -> list[dict]:
    """функция принимает на вход путь в типа "строка" JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        with open(operations_json, encoding="utf-8") as transactions_file:  # попытка открыть файл с кодировкой utf8
            transactions = json.load(transactions_file)
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_transaction(transaction: dict, result: str = "RUB") -> float:
    """Принимает одну транзакцию и возвращает сумму в рублях.
    Если валюта не RUB, используется API-конвертация."""
    logger.info(f'Запуск функции {get_transaction()}')

    try:
        currency = transaction['operationAmount']['currency']['code']
        amount = float(transaction['operationAmount']['amount'])
        logger.info(f'Попытка получения переменных: {currency}б {amount}')

    except KeyError:
        logger.warning(f'Ошибка при получении переменных: {0.0}')
        return 0.0

    if currency == result:
        logger.info(f'Возвращение стоимости RUB: {amount} по курсу на сегодняшний день')
        return amount

    else:
        logger.debug(f'Конвертация валюты в рубль'
                     f'{}')
        return external_api.conversion_transactions(transaction)
