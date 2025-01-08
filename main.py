from src.masks import get_mask_account, get_mask_card_number

numbers_cards = input("введите номер карты: ")
print(get_mask_card_number(numbers_cards))

numbers_accounts = input("введите номер счета: ")
print(get_mask_account(numbers_accounts))
