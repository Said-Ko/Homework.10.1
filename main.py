# from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date

# numbers_cards = input("введите номер карты: ")
# print(get_mask_card_number(numbers_cards))
#
# numbers_accounts = input("введите номер счета: ")
# print(get_mask_account(numbers_accounts))

tested_input = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(tested_input))
print(sort_by_date(tested_input))
