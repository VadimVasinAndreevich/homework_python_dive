class Text:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.validate_str(value)
        setattr(instance, self.param_name, value)

    def validate_str(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.isalpha():
            raise ValueError(f'"{value}" должно содержать только буквы')
        if not value.istitle():
            raise ValueError(f'Первая буква в "{value}" должна быть заглавной')
