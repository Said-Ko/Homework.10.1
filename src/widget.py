from masks import get_date, mask_account_card

user_card = input("Введите тип карты и номер карты: ")
print(mask_account_card(user_card))

users_date = input("Введите дату: ")
print(get_date(users_date))
