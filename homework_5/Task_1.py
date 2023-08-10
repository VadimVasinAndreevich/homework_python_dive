"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
operation_str = "C:\PycharmProjects\homework_GB\homework_5\Task_1.py"


def string_in_tuple(func_str):
    func_str = (func_str.replace('.', '\\')).split("\\")
    x = len(func_str)
    test_list_one = '\\'.join(func_str[0:x-2])
    new_list = []
    for el in range(x):
        if el == 0:
            new_list.append(test_list_one)
        elif el == x-2 or el == x-1:
            new_list.append(func_str[el])
    yield tuple(new_list)


res = string_in_tuple(operation_str)
for el in res:
    print(el)

