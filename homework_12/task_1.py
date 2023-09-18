"""
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Тут тоже добавить дескрипторы.
Также экземпляр должен сообщать средний балл по тестам для каждого предмета
и по оценкам всех предметов вместе взятых.
Итого 4 класса, 3 из них - дескрипторы, плюс обязательно наличие дандера slots
"""

from Tester import Tester
import csv


class Student:
    __slots__ = ('_name', '_surname', '_patronymic', '_file', '_estimation', '_result_test')
    result_subject_test = {}
    result_dict = {}

    def __init__(self, cl_name, cl_surname, cl_patronymic, cl_file):
        self._name = cl_name
        self._surname = cl_surname
        self._patronymic = cl_patronymic
        self._file = cl_file

    def open_file(self):
        with open(self._file, 'r', encoding='utf-8', newline='') as f:
            filereader = csv.DictReader(f, delimiter=',')
            count_estimation = 0
            count_iter_estimation = 0
            for line in filereader:
                self._estimation = list(map(int, line['Оценки'].split()))
                for el in self._estimation:
                    count_estimation += el
                    count_iter_estimation += 1
                self._result_test = list(map(int, line['Баллы'].split()))
                count_result_test = 0
                for el in self._result_test:
                    count_result_test += el
                count_result_test = count_result_test / len(self._result_test)
                subject = line['Предмет']
                self.result_subject_test[subject] = round(count_result_test, 2)
            self.result_subject_test['Средняя оценка всех предметов'] = \
                round(count_estimation / count_iter_estimation, 1)
            self.result_dict[self._surname + " " + self._name + " " + self._patronymic] = self.result_subject_test

    def __str__(self):
        return f'{self.result_dict}'


if __name__ == '__main__':
    name, surname, patronymic, file = 'Архимед', 'Архимедов', 'Архимедович', 'task.CSV'
    test_obj = Tester(name, surname, patronymic, file)
    test_obj.open_file()
    std_one = Student(name, surname, patronymic, file)
    std_one.open_file()
    print(std_one)
    print(Student.__dict__)
