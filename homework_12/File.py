class File:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.validate_file(value)
        setattr(instance, self.param_name, value)

    def validate_file(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if value[value.index('.')+1:len(value)] != 'CSV':
            raise ValueError(f'"{value}" должно быть формата "CSV"')
