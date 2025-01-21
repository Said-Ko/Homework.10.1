from typing import Any
import pytest
from typing import Generator
import random

def card_number_generator(begin_numb, last_numb):
    """ Генератор выдает "рандомный" номер карты в формате XXXX XXXX XXXX XXXX, где Х может быть от 0 до 9"""
    if str(begin_numb).isdigit and str(last_numb).isdigit:
        for numb in range(begin_numb, last_numb):  # Цикл генерации значений
            result_numb = "0" * (16 - len(str(numb))) + str(numb)  # Формирование числа из 16 символов
            yield f"{result_numb[:4]} {result_numb[4:8]} {result_numb[8:12]} {result_numb[12:17]}"
    else:
        yield "Нужно ввести числа"



total = card_number_generator(1,9)

print(next(total))
print(next(total))
print(next(total))
print(next(total))
