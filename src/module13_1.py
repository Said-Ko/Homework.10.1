import csv
# import pandas as pd


transaction_csv = 'transaction/transactions.csv'


# Обратока CSV

# with open(transaction_csv, encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=";")
#     for row in reader:
#
#         print(row)






def read_csv_transactions(file_csv):
    """функция считывания транзакции .CSV формата"""
    transactions = []
    try:
        with open(file_csv, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(row)
                # print(row)
            return transactions
    except Exception:
        return []
#
#
print(read_csv_transactions(transaction_csv))

# transaction_xlsx = 'transaction/transactions.xlsx'
