from math import floor
import re


def binary_calculator(bin1, bin2, operator):
    if (not re.fullmatch("[01]+", bin1)) or not re.fullmatch("[01]+", bin2):
        return "Error"
    if int(bin2) == 0 and operator == "/":
        return "NaN"
    calc = floor(eval(to_dec(bin1) + operator + to_dec(bin2)))
    if 255 < calc or calc < 0:
        return "Overflow"
    return to_bin(calc).zfill(8)


# def to_bin(num):
#     result = ""
#     num = int(num)
#     pow = floor(log2(num))
#     while pow >= 0:
#         if 2**pow <= num:
#             num -= 2**pow
#             result += "1"
#         else:
#             result += "0"
#         pow -= 1
#     return result


def to_bin(num):
    result = "" if num > 0 else "0"
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result


def to_dec(num):
    result = 0
    for pos, digit in enumerate(num[::-1]):
        result += int(digit) * (2**pos)
    return str(result)