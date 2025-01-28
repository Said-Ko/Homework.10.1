from src.generators import transaction_descriptions, filter_by_currency, card_number_generator
from tests.conftest import filter_by_currency_fixture_one, filter_by_currency_fixture_two
import pytest


def test_filter_by_currency_fixture(filter_by_currency_verification):
    assert filter_by_currency(filter_by_currency_verification, "USD") == filter_by_currency_fixture_one
    assert filter_by_currency(filter_by_currency_verification, "RUB") == filter_by_currency_fixture_two


def test_transaction_descriptions():
    result_test_transaction_descriptions = transaction_descriptions()
    assert next(result_test_transaction_descriptions) == "Перевод организации"
    assert next(result_test_transaction_descriptions) == "Перевод со счета на счет"
    assert next(result_test_transaction_descriptions) == "Перевод со счета на счет"
    assert next(result_test_transaction_descriptions) == "Перевод с карты на карту"
    assert next(result_test_transaction_descriptions) == "Перевод организации"


@pytest.mark.parametrize("begin_numb, last_numb, result_generator", [
    ('a', 9, ["Нужно ввести диапазона номеров"]),
    ('1', 'a', ["Нужно ввести диапазона номеров"]),
    (' ', ' ', ["Нужно ввести диапазона номеров"]),
    (1, 3, ['0000 0000 0000 0001',
            '0000 0000 0000 0002'])
])
def test_card_number_generator(begin_numb: int, last_numb: int, result_generator: list[str]) -> None:
    assert list(card_number_generator(begin_numb, last_numb)) == result_generator
