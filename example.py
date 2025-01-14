from typing import Union

import pytest

def mask_account_card(user_card: Union[str]) -> Union[str]:
    """Функция приема типа и номера карты или счета"""
    if not user_card:
        return "0"
    elif user_card[:1].isalpha():
        for letter in user_card:
            if letter.isdigit():
                result_letter = letter
                break
    else:
        return "Введите сначала тип карты, а после номер"
    index_first_digit = user_card.find(result_letter)
    name_card = user_card[:index_first_digit-1].title()
    numb_card = user_card[index_first_digit:]
    if "Счет" in user_card:
        return f"{name_card} **{numb_card[-4:]}"
    else:
        return f"{name_card} {numb_card[0:4]} {numb_card[4:6]}** **** {numb_card[-4:]}"



# user_card = "Visa Classic 6831982476737658"
# print(mask_account_card(user_card))
print(mask_account_card("Maestro 1596 8378 6870 5199"))
