"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ["Елена Павловна", "Анна Дмитриевна", "Виктор Викторович", "Сергей Геннадьевич"]
salaries = [15000, 21000, 37000, 32000]
awards = ["12.45%", "17.32%", "16.55%", "11.76%"]


def dictionary_from_list(list_n, list_s, list_a):
    yield {name: salary * float(award[0:len(award)-1]) / 100 for name, salary, award in zip(list_n, list_s, list_a)}


res = dictionary_from_list(names, salaries, awards)
print(*res)

