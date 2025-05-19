import os
import csv
import pandas as pd

script_dir = os.path.dirname(__file__)
project_root = os.path.dirname(script_dir)  # Папка HomeWork_9.1
transaction_csv = os.path.join(project_root, 'transaction', 'transactions.csv')
transaction_xlsx = os.path.join(project_root, 'transaction', 'transactions_excel.xlsx')


# # обработка данных CSV формата
def read_csv_transactions(file_csv: list[dict]) -> list[dict]:
    """функция считывания транзакции .CSV формата"""
    transactions = []
    try:
        with open(file_csv, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(row)
            return transactions
    except FileNotFoundError:
        return (f"Файл не найден: {file_csv}")


# print(read_csv_transactions(transaction_csv))


# обработка данных .xlsx формата
def read_xlsx_transactions(file_xlsx):
    """функция считывания транзакции .xlsx формата"""
    try:
        df = pd.read_excel(file_xlsx)
        xlsx_transactions = df.to_dict('records')
        return xlsx_transactions
    except Exception:
        return (f'Файл не найден: {file_xlsx}')

# print(read_xlsx_transactions(transaction_xlsx))
