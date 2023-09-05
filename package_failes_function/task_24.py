"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — хэш значения переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""

one = 'one'
two = 2
three = 3
four = 'four'
five = True
six = False


def create_dict_one():
    g = globals()
    test_dict = {}
    for k, v in g.items():
        if k[0] != '_':
            res_k = k
            if type(v) != str:
                res_v = str(v)
            else:
                res_v = v
            test_dict[res_v] = res_k
    test_dict.popitem()
    print(test_dict)


create_dict_one()


def create_dict_two(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        if type(v) != str:
            res_k = str(v)
        else:
            res_k = v
        res_v = k
        new_dict[res_k] = res_v
    print(new_dict)


create_dict_two(one='one', two=2, three=3, four='four', five=True, six=False)
