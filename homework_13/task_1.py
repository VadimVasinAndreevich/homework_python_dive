"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""
"""
Имеется список случайных целых чисел.
Создайте список, в который попадают числа,
описывающие максимальную сплошную возрастающую последовательность.
Порядок элементов менять нельзя.
Одно число - это не последовательность.
"""
import random


def create_list_input():
    list_input = [int(input('введите число: ')) for _ in range(10)]
    length_sequence(list_input)


def create_list():
    my_list = [random.randint(0, 10) for _ in range(0, 10)]
    print(my_list)
    length_sequence(my_list)


def length_sequence(func_list):
    max_iter = 1
    operation_list_three = []
    for el in func_list:
        count = 0
        operation_list_two = []
        while el+count in func_list:
            operation_list_two.append(el+count)
            count += 1
        if count > max_iter:
            operation_list_three = []
            max_iter = count
            operation_list_one = operation_list_two[::len(operation_list_two) - 1]
            operation_list_three.append(operation_list_one)
        elif count > 1 and count == max_iter:
            operation_list_one = operation_list_two[::len(operation_list_two) - 1]
            if operation_list_one not in operation_list_three:
                operation_list_three.append(operation_list_one)
    print_list_seq(operation_list_three)


def print_list_seq(score_list):
    if len(score_list) == 1:
        for el in score_list:
            print(f'{el} так как в списке есть все значения от '
                  f'{el[0]} до {el[1]} и эта последовательность длиннее всех в списке')
    elif len(score_list) > 1:
        for el in score_list:
            print(f'{el} так как в списке есть все значения от '
                  f'{el[0]} до {el[1]} и эта последовательность одна из самых длинных в списке')


def start():
    try:
        create_list_input()
    except ValueError as notice:
        print(f'Вы вводите строковое значение {notice}, а нужно целые числа')
        print('Попробуйте ещё раз')
        start()
    else:
        print('Программа завершена без ошибок')
    finally:
        print('Работа программы завершена')


if __name__ == '__main__':
    start()
