# -*- coding: utf-8 -*-
NUMBERS = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыри',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восем',
    9: 'девять',
    11: 'одинадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'петнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'деветнадцать',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семдесят',
    80: 'восемдесят',
    90: 'девяносто',
    100: 'сто',
    200: 'двесте',
    300: 'триста',
    400: 'четыриста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'деветьсот',
}


def get_string_number(number):
    res_number = []
    res_string = []

    while number > 0:
        number, remainder = divmod(number, 10)
        res_number.append(remainder)

    for i in reversed(res_number):
        res_string.append(NUMBERS[10 ** res_number.index(i) * i])

    return ' '.join(res_string)

if __name__ == '__main__':
    print get_string_number(123)
    print get_string_number(321)
