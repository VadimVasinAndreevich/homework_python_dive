class Grandprotect(Exception):
    pass


class Protect_str(Grandprotect):

    def __init__(self, path_iter, pos_csv, pos_json, pos_pickle):
        self.path_iter = path_iter
        self.pos_csv = pos_csv
        self.pos_json = pos_json
        self.pos_pickle = pos_pickle

    def __str__(self):
        tester = [el for el in (self.path_iter, self.pos_csv, self.pos_json, self.pos_pickle) if type(el) is not str]
        return f'значения собранные в списке {tester} не являются строкой'


class Protect_write(Grandprotect):

    def __init__(self, path_iter, pos_csv, pos_json, pos_pickle):
        self.path_iter = path_iter
        self.pos_csv = pos_csv
        self.pos_json = pos_json
        self.pos_pickle = pos_pickle

    def __str__(self):
        text = ''
        if '\\' not in self.path_iter:
            text += f'Возможно {self.path_iter} не является путём к директории'
        if '.' not in self.pos_csv:
            text += f'{self.pos_csv} не содержит формат\n'
        if '.' not in self.pos_json:
            text += f'{self.pos_json} не содержит формат\n'
        if '.' not in self.pos_pickle:
            text += f'{self.pos_pickle} не содержит формат\n'
        return text


class Protect_form(Grandprotect):

    def __init__(self, pos_csv, pos_json, pos_pickle):
        self.pos_csv = pos_csv
        self.pos_json = pos_json
        self.pos_pickle = pos_pickle

    def __str__(self):
        text = ''
        if self.pos_csv[self.pos_csv.index('.'):len(self.pos_csv)] is not 'CSV':
           text += f'формат файла {self.pos_csv} должен быть "CSV"\n'
        if self.pos_json[self.pos_json.index('.'):len(self.pos_json)] is not 'json':
            text += f'формат файла {self.pos_json} должен быть "json"\n'
        if self.pos_pickle[self.pos_pickle.index('.'):len(self.pos_pickle)] is not 'pickle':
            text += f'формат файла {self.pos_pickle} должен быть "pickle"\n'
        return text