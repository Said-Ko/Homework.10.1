from typing import Union


def mask_account_card(user_card: Union[str, int]) -> Union[str, int]:
    '''Функция приема типа и номера карты или счета'''
    beginning_numb_cards = user_card.rfind(' ')
    card_name = user_card[:beginning_numb_cards]
    card_numb = user_card[beginning_numb_cards + 1:]
    if "Счет" in user_card:
        return (f'{card_name} **{card_numb[-4:]}')
    else:
        return (f'{card_name} {card_numb[0:4]} {card_numb[4:6]}** **** {card_numb[-4:]}')


def get_date(users_date: Union[str]) -> Union[str]:
    """Функция приема даты и возврат в стандартном формате"""
    date_without_time = users_date.find('T')
    only_date = users_date[:date_without_time]
    truth_format_date_list = list(reversed(only_date.split('-')))
    result = '.'.join(truth_format_date_list)
    return result


user_card = input('Введите тип карты и номер карты: ')
print(mask_account_card(user_card))

users_date = input("Введите дату: ")
print(get_date(users_date))
