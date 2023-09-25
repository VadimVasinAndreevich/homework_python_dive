"""
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип экземпляра (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""
import argparse
from logger import operation_log as ol


class Animal:

    def __init__(self, weight, height, pet):
        self.weight = weight
        self.height = height
        self.pet = pet

    def move(self):
        print("I am moving")


class Fish(Animal):

    def __init__(self, weight, height, pet, species):
        super().__init__(weight, height, pet)
        self.__species = species

    def move(self):
        print("i'm fish, i can swim")

    def get_species(self):
        return f"it's {self.__species}, her size {self.weight}x{self.height}"


class Human(Animal):

    def __init__(self, weight, height, pet, species):
        super().__init__(weight, height, pet)
        self.__species = species

    def move(self):
        print("i'm human, i can think")

    def get_species(self):
        return f"it's {self.__species}, his size {self.weight}x{self.height}"


class Factorie:
    obj_x = None
    text_error = ''

    def __init__(self, object_x, weight, height, pet, species):
        if not isinstance(object_x, type):
            self.text_error = ol(object_x, '40_is_type', None)
        elif not isinstance(weight, (int, float)):
            self.text_error = ol(weight, '40_type', 'целое или вещественное число')
        elif weight <= 0:
            self.text_error = ol(weight, '40_value', None)
        elif not isinstance(height, (int,float)):
            self.text_error = ol(height, '40_type', 'целое или вещественное число')
        elif height <= 0:
            self.text_error = ol(height, '40_value', None)
        elif not isinstance(pet, bool):
            self.text_error = ol(pet, '40_type', 'булевое значение')
        elif not isinstance(species, str):
            self.text_error = ol(species, '40_type', 'строка')
        else:
            self.species = species
            self.object_x = object_x
            self.weight = weight
            self.height = height
            self.pet = pet

    def print_info(self):
        if self.pet is True:
            self.obj_x = self.object_x(self.weight, self.height, self.pet, self.species)
            self.obj_x.move()
            return self.obj_x.get_species()
        else:
            return "maybe it's not animal"


def operation_param(*args):
    args = list(args)
    iter_str = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm. '
    for el in range(len(args)):
        count = 0
        for elem in args[el]:
            if elem in '1234567890' and elem not in iter_str:
                count += 1
        if count == len(args[el]):
            args[el] = int(args[el])
        elif count == len(args[el])-1:
            args[el] = float(args[el])
        if args[el] == 'True':
            args[el] = True
        elif args[el] == 'False':
            args[el] = False
    obj_animal = Fish(None, None, None, None)
    obj_one = Factorie(type(obj_animal), args[0], args[1], args[2], args[3])
    return obj_one.print_info()


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('param', metavar='a b c', nargs='*', help='enter a b c separated by a space')
args = parser.parse_args()
print(operation_param(*args.param))
