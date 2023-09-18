class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if type(value) is int:
            self.validate_int(value)
        else:
            self.validate_list(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate_int(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')

    def validate_list(self, value):
        if not isinstance(value, list):
            raise TypeError(f'Значение {value} должно быть списком')
        for el in value:
            if el < self.min_value and self.min_value is not None:
                raise ValueError(f'Значение {el} должно быть больше или равно {self.min_value}')
            if el >= self.max_value and self.max_value is not None:
                raise ValueError(f'Значение {el} должно быть меньше или равно {self.max_value}')
