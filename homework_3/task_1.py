"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
на входе [1,2,3,1,2,5,6] , на выходе [1,2]
"""
operation_list = [1, 2, 3, 1, 2, 5, 6]
duplicate_list = set([el for el in operation_list if operation_list.count(el) > 1])
print(list(duplicate_list))