"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.
"""
"""
Создайте свой модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Вызовите эту функцию из основного файла main.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

from random import randint as ri


class Position:
    def __init__(self, param):
        self.param = param

    def position_obj(self):
        print(self.param)
        if len(set(self.param)) == len(self.param):
            return True
        else:
            return False


class Position_random:
    count = 1
    max_iter = 4

    def pos_ran(self):
        while self.count <= self.max_iter:
            position_list = [f'{ri(1, 9)}:{ri(1, 9)}' for _ in range(0, 8)]
            if len(set(position_list)) == len(position_list):
                print(position_list)
                self.count += 1


if __name__ == '__main__':
    obj_one = Position([f'{ri(1, 9)}:{ri(1, 9)}' for _ in range(0, 8)])
    print(obj_one.position_obj())
    obj_two = Position_random()
    obj_two.pos_ran()
