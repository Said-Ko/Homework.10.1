from typing import Union


# def mask_account_card(user_card: Union[str]) -> Union[str]:
#     """Функция приема типа и номера карты или счета"""
#     beginning_numb_cards = user_card.rfind(" ")
#     card_name = user_card[:beginning_numb_cards]
#     card_numb = user_card[beginning_numb_cards + 1:]
#     if "Счет" in user_card:
#         return f"{card_name} **{card_numb[-4:]}"
#     else:
#         return f"{card_name} {card_numb[0:4]} {card_numb[4:6]}** **** {card_numb[-4:]}"
def mask_account_card(user_card: Union[str]) -> Union[str]:
    """Функция приема типа и номера карты или счета"""
    # if not user_card:
    #     return "0"
    if user_card[:1].isalpha():
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


def get_date(users_date: Union[str]) -> Union[str]:
    """Функция приема даты и возврат в стандартном формате"""

    if users_date is None or not users_date :
        result = "Введите дату."
    elif "T" in users_date:
        date_without_time = users_date.find("T")
        only_date = users_date[:date_without_time]
        truth_format_date_list = list(reversed(only_date.split("-")))
        result = ".".join(truth_format_date_list)
    else:
        truth_format_date_list = list(reversed(users_date.split("-")))
        result = ".".join(truth_format_date_list)
    return result
