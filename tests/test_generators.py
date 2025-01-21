# from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.generators import transaction_descriptions,filter_by_currency
from tests.conftest import filter_by_currency_fixture_one,filter_by_currency_fixture_two
import pytest


def test_filter_by_currency_fixture(filter_by_currency_verification: list) -> None:
    assert next(filter_by_currency(filter_by_currency_verification, "USD")) == filter_by_currency_fixture_one
    assert next(filter_by_currency(filter_by_currency_verification, "RUB")) == filter_by_currency_fixture_two


def test_transaction_descriptions():
    result_test_transaction_descriptions = transaction_descriptions()
    assert next(result_test_transaction_descriptions) == "Перевод организации"
    assert next(result_test_transaction_descriptions) == "Перевод со счета на счет"
    assert next(result_test_transaction_descriptions) == "Перевод со счета на счет"
    assert next(result_test_transaction_descriptions) == "Перевод с карты на карту"
    assert next(result_test_transaction_descriptions) == "Перевод организации"

# def test_card_number_generator():
#     assert next()