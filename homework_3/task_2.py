"""
В большой текстовой строке подсчитать количество встречаемых слов
и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""
operation_string = 'В языке Python строки — это тип данных, который используется для представления текста. ' \
                   'Это один из базовых типов, с которым мы имеем дело в каждом проекте на Python.' \
                   'Когда дело доходит до выбора одинарных или двойных кавычек, нужно быть последовательным. ' \
                   'То есть вы можете использовать и те, и другие, но придерживайтесь одного стиля во всем проекте. ' \
                   'Применять строки и производить различные манипуляции с ними вам придется часто. ' \
                   'Что касается «манипуляций», со строками можно делать множество вещей. ' \
                   'Например, объединять, нарезать, изменять, находить подстроки и многое другое. ' \
                   'В Python строка представляет собой набор символов. ' \
                   'Каждый символ строки имеет индекс — порядковый номер. ' \
                   'Благодаря этой индексации можно получить доступ к конкретному символу в данной строке, ' \
                   'что весьма удобно. Индексация строк Python начинается с нуля ' \
                   'Это означает, что 1-й символ строки имеет индекс 0, 2-й символ имеет индекс 1 и так далее.'
new_string = ''
for sym in operation_string:
    if sym != ',' and sym != '.' and sym != '—':
        new_string += sym.lower()
new_list = [el for el in new_string.split()]
count_set = set([new_list.count(el) for el in new_list])
count = max(count_set)
my_list = []
while count > 1:
    for el in new_list:
        if new_list.count(el) == count and el not in my_list and len(my_list) < 10:
            my_list.append(el)
    count -= 1
print(my_list)











