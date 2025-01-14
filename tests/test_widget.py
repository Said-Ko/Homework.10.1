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



def test_get_date():
    assert get_date("2019-07-03T18:35:29.512364") == '03.07.2019'
    assert get_date("2009T18:35:29.512364") == '2009'
    assert get_date("") == ''



