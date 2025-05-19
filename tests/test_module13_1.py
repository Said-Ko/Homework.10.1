from unittest.mock import patch, mock_open
from src.module13_1 import read_csv_transactions, read_xlsx_transactions
from src.module13_1 import PATH_TO_FILE_CSV, PATH_TO_FILE_XLSX
import pandas as pd


# Тесты для функции read_csv_transactions
def test_read_csv_transactions_find_file() -> list[dict]:
    """Тест CSV файла и возврат данных в виде списка словарей"""
    csv_data = ("date;amount;category\n2023-01-01;100;Food")
    mocked = mock_open(read_data=csv_data)
    with patch("builtins.open", mocked):
        result = read_csv_transactions(PATH_TO_FILE_CSV)
    assert result == [{"date": "2023-01-01", "amount": "100", "category": "Food"}]
    mocked.assert_called_once_with(PATH_TO_FILE_CSV, encoding='utf-8')
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)


def test_read_csv_transactions_empty():
    """Тест обработки пустого CSV файла"""
    mocked = mock_open(read_data='')
    with patch("builtins.open", mocked):
        result = read_csv_transactions(PATH_TO_FILE_CSV)
    assert result == []


# Тесты для функции read_xlsx_transactions
def test_read_xlsx_transactions_find_file() -> None:
    """Тест проверяет корректное чтение XLSX файла и возврат данных в виде списка словарей"""
    test_data = [
        {"date": "2023-01-01", "amount": 1000, "category": "food"},
        {"date": "2023-01-02", "amount": 2000, "category": "hobby"}
    ]
    mock_df = pd.DataFrame(test_data)
    with patch("pandas.read_excel", return_value=mock_df) as mock_read:
        result = read_xlsx_transactions(PATH_TO_FILE_XLSX)
        assert result == test_data
        mock_read.assert_called_once_with(PATH_TO_FILE_XLSX)
        assert isinstance(result, list)
        assert all(isinstance(item, dict) for item in result)
