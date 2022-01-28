# -*- coding: utf-8 -*-

def to_digit(c):
    # коды символов (байтовое представление) идет подряд для цифр
    # ord перевод символ в его номер
    digit = ord(c) - ord('0')
    if 0 <= digit < 10:
        return digit
    else:
        raise ValueError("символ {} не является цифрой", c)


def str_to_int(s):
    if len(s) == 0:
        raise ValueError("строка не содержит цифр")

    # первый символ может быть отрицательным
    negative = 1
    if len(s) > 0 and s[0] == "-":
        negative = -1
        s = s[1:]

    result = 0
    for pos, c in enumerate(reversed(s)):
        digit = to_digit(c)
        result += digit * (10 ** pos)
    return result * negative


if __name__ == '__main__':
    print(str_to_int("-"))
