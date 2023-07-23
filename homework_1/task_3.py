"""
Посчитать сумму цифр любого целого или вещественного
числа, которое введет пользователь. Через строку решать нельзя.\
Можно юзать decimal.
"""

number = input('Введите вещественное или целое число: ')
for symbol in range(len(number)):
    if number[symbol] == '.':
        number_float = float(number)
        while symbol != len(number) - 1:
            number_float *= 10
            symbol += 1
        number = int(number_float)
        break
number = int(number)
sum_nums_number = 0
while number != 0:
    sum_nums_number += number % 10
    number //= 10
print(sum_nums_number)


