import random

text = 'XXXX XXXX XXXX XXXX'
def func1(text):
    new_text = ''
    for i in text:
        if i.isalpha():
            new_text += str(random.randint(1,9))
        else:
            new_text +=i
    return new_text

print(func1(text))

import random

text = 'XXXX XXXX XXXX XXXX'

def func2(text):
    new_text = ''.join(str(random.randint(1,9)) if i.isalpha() else i for i in text)
    return new_text

print(func2(text))

def func3():
    unless_numb = '0000 0000 0000 0000'
    new_code = ''
    for numb in unless_numb:
        if numb.isdigit():
            new_code += str(random.randint(1, 9))
            # numb.replace(str(random.randint(1, 9)))
        else:
            new_code +=numb
    return new_code

print(func3())

# def random_number_generator(start, stop):
#     while True:
#         yield random.randint(start, stop)


# def func1(start, stop):
#     a = []
#     while len(a) < 19:
#         if len(a) % 4 == 0:
#             a.append(' ')
#         elif True:
#             a.append(random.randint(start, stop+1))
#
# print(func1(1,9))

# def random_number_generator(start, stop):
#     while True:
#         yield random.randint(start, stop)
#
# print(next(random_number_generator(8, 12)))
# print(next(random_number_generator(8, 12)))
# print(next(random_number_generator(8, 12)))
