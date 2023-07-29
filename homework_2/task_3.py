"""
Напишите программу, которая принимает две строки вида
“a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

print('Введите дробь вида "a/b"')
fraction_first = input('Введите первую дробь: ')
frac_first = None
denom_first = None
for el in range(len(fraction_first)):
    if fraction_first[el] == '/':
        frac_first = fraction_first[:el]
        denom_first = fraction_first[el+1:]
fraction_second = input('Введите вторую дробь: ')
frac_second = None
denom_second = None
for el in range(len(fraction_second)):
    if fraction_second[el] == '/':
        frac_second = fraction_second[:el]
        denom_second = fraction_second[el+1:]
sum_fractions = int(frac_first) * int(denom_second) + \
                    int(frac_second) * int(denom_first)
denom_sum = int(denom_first) * int(denom_second)
print(Fraction(sum_fractions, denom_sum))
for el in range(2, sum_fractions + 1):
    if sum_fractions % el == 0 and denom_sum % el == 0:
        sum_fractions //= el
        denom_sum //= el
multi_fractions = int(frac_first) * int(frac_second)
multi_denom = int(denom_first) * int(denom_second)
print(Fraction(multi_fractions, multi_denom))
for el in range(2, multi_fractions + 1):
    if multi_fractions % el == 0 and multi_denom % el == 0:
        multi_fractions //= el
        multi_denom //= el
print(f'{fraction_first} + {fraction_second} = {sum_fractions}/{denom_sum}')
print(f'{fraction_first} * {fraction_second} = {multi_fractions}/{multi_denom}')
