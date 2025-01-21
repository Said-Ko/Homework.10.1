from typing import Dict, Any, List, Union, Generator
from tests.conftest import transactions
import random




#
def filter_by_currency(transactions: List, currency: str = "USD") -> None:
    """ Функция принимает на вход список словарей, представляющая транзакции,
    на выходе возвращает итератор, где валюта операции соответсветствует заданной"""
    result_filter_by_currency = list(filter(lambda x: x["operationAmount"]["currency"]["code"]== currency, transactions))
    yield result_filter_by_currency


def transaction_descriptions(start=1):
    """ Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    while start < len(transactions):
        for transaction in transactions:
            yield transaction["description"]
            start += 1



def card_number_generator():
    """ Генератор выдает номер карты в диапозоне XXXX XXXX XXXX XXXX, где Х может быть от 0 до 9"""
    default_code = '0000 0000 0000 0000'
    new_code = ''
    for numb in default_code:
        if numb.isdigit():
            new_code += str(random.randint(1,9))
        else:
            new_code += numb
    yield new_code




