"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""
import logging
import argparse


def dictionary_from_list(list_n, list_s, list_a):
    yield {name: salary * float(award[0:len(award)-1]) / 100 for name, salary, award in zip(list_n, list_s, list_a)}


def complex_list(*args):
    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
             'в строке {lineno:03d} функция "{funcName}()" ' \
             'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
    list_name = []
    list_salary = []
    list_award = []
    for el in args:
        iter_str = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбюё.% '
        count = 0
        for elem in el:
            if elem in '1234567890' and elem not in iter_str:
                count += 1
        if count == len(el):
            list_salary.append(int(el))
        elif count == 0:
            list_name.append(el)
        elif count == len(el)-2:
            list_award.append(el)
        else:
            logging.warning(f'возможно в параметре "{el}" допущена ошибка')
    set_test = {len(list_name), len(list_salary), len(list_award)}
    if len(set_test) > 1:
        logging.error(f'Неравное количество элементов в списках {list_name}\n{list_salary}\n{list_award}')
    for el in list_name:
        res_test = el.split()
        for elem in res_test:
            if not elem.istitle():
                logging.warning(f'Имя начинается не с заглавной буквы "{el}", список: {list_name}')
    res = dictionary_from_list(list_name, list_salary, list_award)
    return res


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('param', metavar='a b c', nargs='*', help='enter a b c separated by a space')
args = parser.parse_args()
print(*complex_list(*args.param))
