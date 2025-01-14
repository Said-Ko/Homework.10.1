from src.masks import get_mask_card_number, get_mask_account

import pytest

from typing import Union


@pytest.mark.parametrize('card_number, hidden_card_number', [
    ('1234123412341234', '1234 12** **** 1234'),
    (1234123412341234, '1234 12** **** 1234'),
    ('1234', 'Введен некорректный номер карты'),
    ('Any_text', 'Введен некорректный номер карты'),
    ("", "0"),
    ({}, "0"),
    ([], "0")
])
def test_get_mask_card_number(card_number: Union[str, int], hidden_card_number: Union[str,int]) -> None:
    assert get_mask_card_number(card_number) == hidden_card_number


@pytest.mark.parametrize('get_account, hidden_account',[
    ('1234123412344134324', '**4324'),
    (1234123412344134324, '**4324'),
    ('Any_text', 'введены не корректные данные'),
    ([],'0')
])

def test_get_mask_account(get_account: Union[str,int], hidden_account: Union[str]) -> None:
    assert get_mask_account(get_account) == hidden_account

