import json
import os
from src.external_api import conversion_transactions

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
    try:
        currency = transaction['operationAmount']['currency']['code']
        amount = float(transaction['operationAmount']['amount'])
    except KeyError:
        return 0.0
    if currency == result:
        return amount
    else:
        return conversion_transactions(transaction)
