"""
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
2.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

import os
import random


VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def generate_name(min_len_name, max_len_name):
    len_name = random.randint(min_len_name, max_len_name)
    name = ''
    for i in range(len_name):
        if i % 2 == 1:
            name += random.choice(VOWELS)
        else:
            name += random.choice(CONSONANTS)
    return name


def create_files(extension: str, min_len_name: int = 10, max_len_name: int = 20,
                 min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 7,
                 catalogue_name: str = '') -> None:
    if catalogue_name not in os.listdir():
        os.mkdir(catalogue_name)
    for i in range(amount_file):
        filename = generate_name(min_len_name, max_len_name)
        file_size = random.randint(min_size_file, max_size_file)
        data = bytes((random.randint(0, 255)) for _ in range(file_size))
        with open(f"{catalogue_name}/{filename}.{extension}", 'wb') as f:
            f.write(data)


def rename_name(part_orig_name: list, end_name: str, exp_file: str, count_num: int = 3,
                catalogue_name: str = '') -> None:
    res = os.listdir(catalogue_name)
    sum_part_name = len(part_orig_name[0]) + len(end_name) + 2
    for el in range(len(res)):
        if len(str(el)) < count_num and res[el][res[el].index('.')-1] not in [str(elem) for elem in range(10)]:
            os.rename(f'{catalogue_name}/{res[el]}',
                      f'{catalogue_name}/{part_orig_name[el]}_{end_name}_{el}.{exp_file}')
    res_one = os.listdir(catalogue_name)
    for el in range(len(res_one)):
        os.rename(f'{catalogue_name}/{res_one[el]}',
                  f'{catalogue_name}/{res_one[el][0:sum_part_name]}{el+1}.{exp_file}')


if __name__ == '__main__':
    create_files('py', catalogue_name='output')
    rename_name([el[3:6] for el in os.listdir('output')], 'task', 'py', catalogue_name='output')
