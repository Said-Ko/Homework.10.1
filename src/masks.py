from typing import Union

def get_mask_card_number(number_card: Union[ int, str]) -> str:
    """Функция принимает на вход номер карты и шифрует его"""
    str_number_card = str(number_card)
    if number_card is None or not number_card:  # Если в номер карты передается пустой список или ничего не передается
        result_number_card = "0" # переопределил его как "0"
    elif " " in str_number_card:
        str_number_card = str_number_card.replace(" ", "")
    elif str_number_card.isdigit() and len(str_number_card) == 16:
        result_number_card = f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"
    else:
        result_number_card = "Введен некорректный номер карты"
    return result_number_card

def get_mask_account(numbers_accounts: Union[str,int]) -> Union[str]:
    """Функция приема номера счета и шифрует его"""

    str_numbers_accounts = str(numbers_accounts)
    if numbers_accounts is None or not numbers_accounts: # Если в номер счета передается пустой список или ничего не передается
        result_number_accounts = "0" # переопределил его как "0"
    elif str_numbers_accounts.isdigit():
        result_number_accounts = f"**{str_numbers_accounts[-4:]}"
    else:
        result_number_accounts = "введены не корректные данные"
    return result_number_accounts

