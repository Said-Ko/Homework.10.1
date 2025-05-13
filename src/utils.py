import json
from src.external_api import conversion_transactions


def check_transactions(operation_json: str) -> list[dict]:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        transactions = json.load(open(operation_json, encoding="utf8"))  # попытка открыть файл с кодировкой utf8
    except FileNotFoundError:  # если файл не найден, возвращает пустой список
        return []

    except json.decoder.JSONDecodeError:  # Если файл не удалось декодировать
        return []

    else:  # возвращает список из файла
        return transactions


def get_transaction(transactions: list[dict]) -> float:
    """ Фунция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
    if isinstance(transactions, dict):  # если класс не список, конвертируем объект в список
        transactions = [transactions]

    for transaction in transactions:  # обработка каждого элемента внутри трансакции
        if transaction['operationAmount']['currency'][
            'code'] == "RUB":  # если значение равно рублю, возвращает сумму транзакции
            return float(transaction['operationAmount']['amount'])
        elif transaction['operationAmount']['currency']['code'] == ("USD" or "EUR"):
            # если значение равно доллару или евро, сумму в рублях через конвертацию через API
            return float(conversion_transactions(transaction))
