from math import floor
import re

# Performs math on binary numbers, returning a binary number
def binary_calculator(bin1, bin2, operator):
    if (not re.fullmatch("[01]+", bin1)) or not re.fullmatch("[01]+", bin2): # Check for binary numbers only (1s and 0s only)
        return "Error"
    if int(bin2) == 0 and operator == "/": # Check for division by 0
        return "NaN"
    calc = floor(eval(to_dec(bin1) + operator + to_dec(bin2))) # Convert the numbers to decimal to do math on them, then calculate and floor the result
    if 255 < calc or calc < 0: # Check for negatives and numbers larger than 8 bits (255)
        return "Overflow"
    return to_bin(calc).zfill(8) # Convert the result back to binary and make it 8 bits long by padding the beginning with 0s


# Other decimal to binary function. Longer and uses logs
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


# Convert a decimal number to binary
def to_bin(num):
    result = "" if num > 0 else "0" # Check for 0, in which case 0 is returned
    while num > 0: # Does some math
        result = str(num % 2) + result
        num //= 2
    return result


# Convert a binary number to decimal
def to_dec(num):
    result = 0
    for pos, digit in enumerate(num[::-1]): # Iterate through the number, reversed so that 0 corresponds with the first digit
        result += int(digit) * (2**pos) # Each digit is multiplied by a power of 2 depending on its position in the number
    return str(result)