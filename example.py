from typing import Dict, Any

# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))

print(filter_by_currency({"id": 939719570,
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
 }
))
