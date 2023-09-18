from Range import Range
from Text import Text
from File import File
import csv


class Tester:
    name = Text()
    surname = Text()
    patronymic = Text()
    file = File()
    estimation = Range(2, 5)
    result_test = Range(0, 100)

    def __init__(self, name, surname, patronymic, file):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.file = file

    def open_file(self):
        with open(self.file, 'r', encoding='utf-8', newline='') as file:
            filereader = csv.DictReader(file, delimiter=',')
            for line in filereader:
                self.estimation = list(map(int, line['Оценки'].split()))
                self.result_test = list(map(int, line['Баллы'].split()))
