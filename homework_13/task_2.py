"""
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип экземпляра (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


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

    def __init__(self, object_x, weight, height, pet, species):
        if not isinstance(object_x, type):
            raise TypeError(f'{object_x = } не содержит тип объекта')
        else:
            self.object_x = object_x
        if not isinstance(weight, (int, float)):
            raise TypeError(f'{weight = } не является вещественным или целым числом')
        if weight <= 0:
            raise ValueError(f'параметр {weight = } не может быть нулевым или иметь отрицательное значение')
        else:
            self.weight = weight
        if not isinstance(height, (int, float)):
            raise TypeError(f'{height = } не является вещественным или целым числом')
        if height <= 0:
            raise ValueError(f'параметр {height = } не может быть нулевым или иметь отрицательное значение')
        else:
            self.height = height
        if not isinstance(pet, bool):
            raise TypeError(f'{pet = } не является булевым значением')
        else:
            self.pet = pet
        if not isinstance(species, str):
            raise TypeError(f'{species = } не является строкой')
        else:
            self.species = species

    def print_info(self):
        if self.pet is True:
            self.obj_x = self.object_x(self.weight, self.height, self.pet, self.species)
            self.obj_x.move()
            return self.obj_x.get_species()
        else:
            return "maybe it's not animal"


if __name__ == '__main__':
    obj_animal = Fish(None, None, None, None)
    obj_one = Factorie(type(obj_animal), 400, 120, True, 'shark')
    print(obj_one.print_info())
    obj_animal = Human(None, None, None, None)
    obj_two = Factorie(type(obj_animal), 180, 60, True, 'homo sapiens')
    print(obj_two.print_info())