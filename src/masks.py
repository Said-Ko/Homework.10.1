import logging
# import datetime
import os
from typing import Union

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('masks')  # Создаем логгер с именем 'masks'
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования DEBUG
logger.handlers.clear()  # Удаляем все существующие обработчики (если есть)
file_handler = logging.FileHandler('logs/masks.log', encoding="utf-8")  # Создаем обработчик для записи логов в файл
# Настраиваем формат записей в логе
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
file_handler.setFormatter(file_formatter)  # Применяем форматтер к обработчику
logger.addHandler(file_handler)  # Добавляем обработчик к логгеру


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и шифрует его"""
    logger.info(f'Начало работы функции "get_mask_card_number". Входные данные: {number_card}')

    str_number_card = str(number_card)
    if number_card is None or not number_card:  # Если в номер карты передается пустой список или ничего не передается
        result_number_card = "0"  # переопределил его как "0
        logger.debug(f'длина карты не соответствует факту {result_number_card}')

    elif 16 <= len(str_number_card) <= 20:
        if " " in str_number_card:
            logger.debug('Произведена замена символов с " " на ""')
            str_number_card = str_number_card.replace(" ", "")

            if str_number_card.isdigit() and len(str_number_card) == 16:
                logger.info(f'Номер карты прошел валидацию: {str_number_card}')
                result_number_card = f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"

        elif str_number_card.isdigit() and len(str_number_card) == 16:
            logger.info(f'Номер карты прошел валидацию: {str_number_card}')
            result_number_card = f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"

        else:
            logger.error(f'Введен некорректный номер карты: {str_number_card}')
            result_number_card = "Введен некорректный номер карты"

    else:
        logger.error(f'Введен некорректный номер карты: {str_number_card}')
        result_number_card = 'Введен некорректный номер карты'

    logger.info(f'Окончание работы функции "get_mask_card_number". Результат обработки: {result_number_card}')
    return result_number_card


def get_mask_account(numbers_accounts: Union[str, int]) -> Union[str]:
    """Функция приема номера счета и шифрует его"""
    logger.info(f'Начало обработки функции "get_mask_account". Входные данные: {numbers_accounts}')
    str_numbers_accounts = str(numbers_accounts)

    # Если номер счета пустой список или ничего не передается
    if str_numbers_accounts is None or not str_numbers_accounts:
        logger.error(f'Если номер счета пустой: {numbers_accounts}')
        result_number_accounts = "0"  # переопределил его как "0"

    elif str_numbers_accounts.isdigit():
        logger.info(f'номер счета прошел валидацию: {str_numbers_accounts}')
        result_number_accounts = f"**{str_numbers_accounts[-4:]}"

    else:
        logger.error(f'Введены не корректные данные: {str_numbers_accounts}')
        result_number_accounts = "введены не корректные данные"

    logger.info(f'Окончание работы функции "get_mask_account". Результат обработки: {result_number_accounts}')
    return result_number_accounts

# if __name__ == '__main__':
#     get_mask_card_number("1234567812345678")
#     get_mask_account("1234567890")
