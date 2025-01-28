from typing import List, Generator, Dict
from tests.conftest import transactions


def filter_by_currency(transactions: List[Dict], currency: str = "USD") -> None:
    """ Функция принимает на вход список словарей представляющая транзакции,
    на выходе возвращает итератор, где валюта соответсветствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(start=1):
    """ Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    while start < len(transactions):
        for transaction in transactions:
            yield transaction["description"]
            start += 1


def card_number_generator(begin_numb: int, last_numb: int) -> Generator:
    """ Генератор выдает номер карты в формате XXXX XXXX XXXX XXXX, где Х может быть от 0 до 9"""
    if type(begin_numb) is int and type(last_numb) is int:
        for numb in range(begin_numb, last_numb):  # Цикл генерации значений
            result_numb = "0" * (16 - len(str(numb))) + str(numb)  # Формирование числа из 16 символов
            yield f"{result_numb[:4]} {result_numb[4:8]} {result_numb[8:12]} {result_numb[12:17]}"
    else:
        yield "Нужно ввести диапазона номеров"
