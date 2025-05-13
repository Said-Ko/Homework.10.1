from src.utils import get_transaction, check_transactions
from unittest.mock import patch


def test_get_transaction():
    """ Функция проверят пустой файл"""
    assert get_transaction('') == []


@patch("requests.get")
def test_get_transaction(mock_get):
    """ Функция проверят пустой файл"""
    assert get_transaction() == []

