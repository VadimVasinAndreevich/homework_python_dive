"""
Напишите функцию для транспонирования матрицы
"""

import random


def create_list():
    pull_list = []
    b = 3
    y = 1
    while y <= b:
        res = []
        i = 1
        while i <= b:
            res.append(random.randint(0, 100))
            i += 1
        pull_list.append(res)
        y += 1
    print(pull_list)
    print()
    matrix_original(pull_list)
    print('Транспонированная матрица:')
    print()
    matrix_trans(pull_list)


def matrix_original(operation_list):
    for el in operation_list:
        matrix_str = ''
        for elem in el:
            p = 7
            test_str = ''
            i = 1
            while i != p - len(str(elem)):
                test_str += ' '
                i += 1
            matrix_str += str(elem) + test_str
        print(matrix_str)
        print()


def matrix_trans(operation_list):
    x = 0
    while x <= len(operation_list)-1:
        matrix_str = ''
        for el in operation_list:
            for elem in range(len(el)):
                if elem == x:
                    p = 7
                    test_str = ''
                    i = 1
                    while i != p - len(str(el[elem])):
                        test_str += ' '
                        i += 1
                    matrix_str += str(el[elem]) + test_str
        print(matrix_str)
        if x != len(operation_list)-1:
            print()
        x += 1


create_list()
