from unittest.mock import mock_open, patch
from src.utils import PATH_TO_FILE
from src.utils import check_transactions_json, get_transaction


# тесты check_transactions_json
def test_check_transactions_json() -> None:
    """
    Тест соответствует требованиям (ключ : значение)
    """
    mocked_open = mock_open(read_data='{"key" : "value"}')
    with patch("builtins.open", mocked_open):
        result = check_transactions_json(PATH_TO_FILE)
    assert result == []
    mocked_open.assert_called_once_with(PATH_TO_FILE, encoding='utf-8')


def test_check_transactions_json_file_empty() -> None:
    """
    Тест проверяет json пустой или нет
    """
    mocked_open = mock_open(read_data="[]")
    with patch("builtins.open", mocked_open):
        result = check_transactions_json(PATH_TO_FILE)
    assert result == []
    mocked_open.assert_called_once_with(PATH_TO_FILE, encoding='utf-8')


# тесты get_transaction
def test_get_transaction_rub():
    """Тест рубля"""
    rub_transaction = {"operationAmount": {"amount": "5432.10", "currency": {"code": "RUB"}}}
    result = get_transaction(rub_transaction)
    assert result == 5432.10
    assert isinstance(result, float)


def test_get_transaction_key_error():
    """Ошибка ключа"""
    rub_transaction = {"operationAmount": {"currency": {"code": "RUB"}}}
    result = get_transaction(rub_transaction)
    assert result == 0.0


def test_get_transaction_not_rub():
    """Иная валюта"""
    not_rub_transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    with patch('src.external_api.conversion_transactions') as mock_convert:
        mock_convert.return_value = 9000.00
        print("Mocked function:", mock_convert)
        result = get_transaction(not_rub_transaction)
        # print("Actual result:", result)
        assert result == 9000.00
        assert isinstance(result, float)
        mock_convert.assert_called_once_with(not_rub_transaction)
