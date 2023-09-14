"""
Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения,
умножения матриц
Добавить документации к классу и методам класса.
Добавить обработку некорректных значений.
"""
from random import randint as ri


class Matrix:
    """
    класс для работы с матрицами
    """
    def __init__(self, work_list):
        if not (isinstance(work_list, list)):
            raise TypeError('тип входящего объекта должень быть список (list)')
        for el in work_list:
            if not (isinstance(el, list)):
                raise TypeError('список должен содержать элементы типа данных список (list)')
        self.work_list = work_list

    def __str__(self):
        res = ''
        for el in self.work_list:
            for elem in range(len(el)):
                if el[elem] < 10:
                    res = res + str(el[elem]) + '      '
                elif el[elem] >= 10:
                    res = res + str(el[elem]) + '     '
            res = res + '\n'
        return res

    def __eq__(self, other):
        if len(self.work_list) == len(other.work_list):
            print('В матрицах одинаковое количество строк')
        if len(self.work_list[0]) == len(other.work_list[0]):
            print('В матрицах одинаковое количество столбцов')
        return 'сравнение матриц на равенство завершено'

    def __lt__(self, other):
        if len(self.work_list) < len(other.work_list):
            print('В первой матрице количество строк меньше чем во второй')
        if len(self.work_list[0]) < len(other.work_list[0]):
            print('В первой матрице количество столбцов меньше чем во второй')
        return 'сравнение матриц на меньшинство завершено'

    def __gt__(self, other):
        if len(self.work_list) > len(other.work_list):
            print('В первой матрице количество строк больше чем во второй')
        if len(self.work_list[0]) > len(other.work_list[0]):
            print('В первой матрице количество столбцов больше чем во второй')
        return 'сравнение матриц на большинство завершено'

    def __add__(self, other):
        result_list = []
        for el in self.work_list:
            for elem in other.work_list:
                if self.work_list.index(el) == other.work_list.index(elem):
                    self.element_list = []
                    for i_el in range(len(el)):
                        for i_elem in range(len(elem)):
                            if i_el == i_elem:
                                self.element_list.append(el[i_el] + elem[i_elem])
                    result_list.append(self.element_list)
        print('Сложение матриц')
        return result_list

    def __mul__(self, other):
        result_list = []
        for el in self.work_list:
            for elem in other.work_list:
                if self.work_list.index(el) == other.work_list.index(elem):
                    self.element_list = []
                    for i_el in range(len(el)):
                        for i_elem in range(len(elem)):
                            if i_el == i_elem:
                                self.element_list.append(el[i_el] * elem[i_elem])
                    result_list.append(self.element_list)
        print('Умножение матриц')
        return result_list

    def generate(self):
        """
        функция для создания матрицы с рандомными значениями
        """
        all_list = []
        i = ri(1, 9)
        j = ri(1, 9)
        while len(all_list) != i:
            part_list = []
            while len(part_list) != j:
                part_list.append(ri(1, 10))
            all_list.append(part_list)
        return all_list

    def correct(self):
        """
        функция для корректировки данных
        """
        for el in range(len(self.work_list)):
            for elem in range(len(self.work_list[el])):
                if type(self.work_list[el][elem]) != int:
                    print(f'в {el+1} строке, {elem+1} столбце, значение {self.work_list[el][elem]} не является'
                          f' типом - "целое число" и было заменено на "0"')
                    self.work_list[el][elem] = 0
        return self.work_list


if __name__ == '__main__':
    """
    основной код программы
    """
    obj_matrix = Matrix([])
    obj_matrix_1 = obj_matrix.generate()
    obj_matrix = Matrix([])
    obj_matrix_2 = obj_matrix.generate()
    obj_matrix_1 = Matrix(obj_matrix_1)
    obj_matrix_2 = Matrix(obj_matrix_2)
    print('матрица 1:')
    print(obj_matrix_1)
    print('матрица 2:')
    print(obj_matrix_2)
    print(obj_matrix_1 == obj_matrix_2)
    print(obj_matrix_1 < obj_matrix_2)
    print(obj_matrix_1 > obj_matrix_2)
    print()
    obj_matrix_3 = Matrix(obj_matrix_1 + obj_matrix_2)
    print(obj_matrix_3)
    obj_matrix_4 = Matrix(obj_matrix_1 * obj_matrix_2)
    print(obj_matrix_4)
    obj_matrix_5 = Matrix([[1, 2, 3], [4, 'tr', 6], [7, 8, 9]])
    obj_matrix_6 = Matrix([[1, '2', 3], [4, 5, 6], [7, 8, 9]])
    try:
        obj_matrix_7 = Matrix(obj_matrix_5 + obj_matrix_6)
        print(obj_matrix_7)
        obj_matrix_8 = Matrix(obj_matrix_5 * obj_matrix_6)
        print(obj_matrix_8)
        print('неккоректных значений нет')
    except TypeError:
        obj_matrix_5 = Matrix(obj_matrix_5.correct())
        print(obj_matrix_5)
        obj_matrix_6 = Matrix(obj_matrix_6.correct())
        print(obj_matrix_6)
    finally:
        obj_matrix_7 = Matrix(obj_matrix_5 + obj_matrix_6)
        print(obj_matrix_7)
        obj_matrix_8 = Matrix(obj_matrix_5 * obj_matrix_6)
        print(obj_matrix_8)
    obj_matrix_9 = Matrix([(1, 2, 3), [4, 'tr', 6], [7, 8, 9]])
    print(obj_matrix_9)
