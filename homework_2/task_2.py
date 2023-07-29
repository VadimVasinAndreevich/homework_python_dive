"""
Напишите программу, которая получает целое число и
возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

number = int(input('Введите целое число: '))
number_operation = number
if number < 0:
    number *= -1
work_str = '0123456789abcdef'
hex_numbs_str = ''
operation_str = ''
start_str = '0x'
while number > 16:
    res = number % 16
    number //= 16
    hex_numbs_str += work_str[res]
hex_numbs_str += work_str[number]
for symbol in reversed(hex_numbs_str):
    operation_str += symbol
if number_operation < 0:
    print('-' + start_str + operation_str)
else:
    print(start_str + operation_str)
print(hex(number_operation))
