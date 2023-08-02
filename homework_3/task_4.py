"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 10) многочлена и записать как многочлен степени k.
"""

import random


def param():
    natural_power = int(input('Введите натуральную степень числа: '))
    test_str = ''
    test_list = []
    count = 0
    operation(natural_power, test_str, test_list, count)


def random_str():
    return f' {random.choice("+-")} '


def operation(natural_power, test_str, test_list, count):
    while len(test_list) != natural_power + 1:
        test_list.append(random.randint(0, 10))
    for el in range(natural_power, 0, -1):
        if el != 1 and test_list[count] != 0 and test_list[count] != 1:
            test_str += str(test_list[count]) + 'x^' + str(el) + random_str()
        elif test_list[count] == 0:
            test_str += ''
        elif el != 1 and test_list[count] == 1:
            test_str += 'x^' + str(el) + random_str()
        elif el == 1 and test_list[count] != 1:
            test_str += str(test_list[count]) + 'x' + random_str() + str(test_list[count+1])
        elif el == 1 and test_list[count] == 1:
            test_str += 'x' + random_str() + str(test_list[count+1])
        count += 1
    print(f'{test_str} = 0, при списке {test_list}')
    answer = input('Продолжить? - "да" или "нет": ')
    if answer == 'да':
        param()
    else:
        print('Программа остановлена')


param()
