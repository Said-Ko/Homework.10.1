from src.widget import mask_account_card, get_date

import pytest

from typing import Union


@pytest.mark.parametrize("get_name_account_card, hidden_name_account_card",[
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("MasterCard 7158300734726758", "Mastercard 7158 30** **** 6758"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 6468 6473 6788 9477 9589", "Счет **9589"),
    # ("Maestro 1596 8378 6870 5199", "Maestro 1596 83** **** 5199"),
    # ("Maestro 1234 1596 8378 5199", "Maestro 1234 15** **** 5199"),
    ("", "Введите сначала тип карты, а после номер"),
    ("1596837868705199 Maestro", "Введите сначала тип карты, а после номер")


])
def test_mask_account_card(get_name_account_card: Union [str,int], hidden_name_account_card: Union[str,int]) -> None:
    assert mask_account_card(get_name_account_card) == hidden_name_account_card


@pytest.mark.parametrize("wrone_write_date, true_write_date",[
    ("2023-03-11T02:26:18.671407", "11.03.2023"),
    ("", "Введите дату."),
    ([], "Введите дату."),
    ("2023-03-11", "11.03.2023"),
])
def test_get_date(wrone_write_date: str, true_write_date: str) -> None:
    assert get_date(wrone_write_date) == true_write_date


