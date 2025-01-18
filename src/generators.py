from typing import Dict, Any, List, Union

transactions = {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },{
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
         }


def filter_by_currency(transactions: Dict, currency: str = "USD") -> None:
    """ Функция принимает на вход список словарей, представляющая транзакции,
    на выходе возвращает итератор, где валюта операции соответсветствует заданной"""
    for transaction in transactions:
        if transaction.get["operationAmount"]["name"]["currency"] == currency: # исходя из примера мы понимаем какой словарь будет на входе
            yield transaction




def transaction_descriptions(transactions):
    """ Генератор примает список словарей и возвращает описание каждой операции по очереди"""
    start = 0 #
    while start < len(transactions):
        yield transactions[start]["description"]
        start += 1

# def card_number_generator(start, stop):
#     """ Генератор выдает номер карты в диапозоне XXXX XXXX XXXX XXXX, где Х может быть от 0 до 9"""
#     while True:






print(filter_by_currency(transactions))
print(transaction_descriptions(transactions))



