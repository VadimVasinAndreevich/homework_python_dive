from random import randint as r
import csv
from typing import Callable
import json
import os


def main_b(func: Callable):
    my_dict = {}

    def quadratic_equation(name_file):
        func(name_file)
        with open(name_file, 'r', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            for i, line in enumerate(csv_file):
                if i > 0:
                    a = int(line[0])
                    b = int(line[1])
                    c = int(line[2])
                    d = b ** 2 - 4 * a * c
                    if d > 0:
                        x1 = -b - d ** (1 / 2) / (2 * a)
                        x2 = -b + d ** (1 / 2) / (2 * a)
                        my_dict[f"Уравнение {i}"] = [f'{x1 = }', f'{x2 = }']
                    elif d == 0:
                        x1 = -b / (2 * a)
                        my_dict[f"Уравнение {i}"] = [f'{x1 = }', False]
                    else:
                        my_dict[f"Уравнение {i}"] = [False, False]
        return my_dict
    return quadratic_equation


def main_a(func: Callable):
    def create_json(dict_for_json, name_file):
        func(dict_for_json, name_file)
        with open(name_file, 'w', newline='', encoding='utf-8') as f:
            json.dump(dict_for_json, f, indent=2, separators=(',', ':'), ensure_ascii=False)
        return f'Запись в {name_file} - завершена'
    return create_json


@main_b
def generate_read_csv(name):
    if name not in os.listdir():
        with open(name, 'w', newline='', encoding='utf-8') as f:
            f.write(f'"a","b","c"\n')
    with open(name, 'r+', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f)
        abc = list(csv_file)
        for _ in range(1, r(101, 902)):
            a, b, c = r(-999, 1000), r(-999, 1000), r(-999, 1000)
            if list(f'{a}{b}{c}') not in abc and a != 0:
                abc.append(list(f'{a}{b}{c}'))
                f.write(f'{a},{b},{c}\n')
    return name


@main_a
def main_json(res: dict, name: str):
    return res, name


if __name__ == '__main__':
    result = generate_read_csv("test_1.CSV")
    print(main_json(result, "test_1.json"))
