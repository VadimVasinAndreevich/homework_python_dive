"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.
"""
"""
1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов
в ней с учётом всех вложенных файлов и директорий.
2.Соберите из созданных на уроке и в рамках домашнего задания функций пакет
для работы с файлами разных форматов.
"""

import os
import json
import pickle


class Write_inf_dir:
    my_dict_list = []
    all_iter_size = 0

    def __init__(self, path_iter, pos_csv, pos_json, pos_pickle):
        self.path_iter = path_iter
        self.pos_csv = pos_csv
        self.pos_json = pos_json
        self.pos_pickle = pos_pickle

    def write_file(self):
        with open(self.pos_csv, 'w', newline='', encoding='utf-8') as f_write:
            f_write.write(f"'DIRECTORY_NAME','FILE_NAME','SIZE_FILE','SIZE_FILES_DIRECTORY','SIZE_DIRECTORY'\n")
            for dir_path, dir_name, file_name in os.walk(self.path_iter):
                size_score = 0
                for el in file_name:
                    size = os.path.getsize(f'{dir_path}\\{el}')
                    size_score += size
                    f_write.write(f"{dir_path},{el},{size}\n")
                f_write.write(f"{dir_path},False,False,{size_score}\n")
                self.all_iter_size += size_score
            f_write.write(f"{self.path_iter},False,False,False,{self.all_iter_size}\n")
        with open(self.pos_json, 'w', newline='', encoding='utf-8') as f_write:
            for dir_path, dir_name, file_name in os.walk(self.path_iter):
                size_score = 0
                for el in file_name:
                    size = os.path.getsize(f'{dir_path}\\{el}')
                    size_score += size
                my_dict = {
                    dir_path: {k: os.path.getsize(f'{dir_path}\\{k}') for k in file_name},
                    'SIZE_FILES_DIRECTORY': size_score,
                }
                self.my_dict_list.append(my_dict)
            iter_dict = {self.path_iter: self.my_dict_list, 'SIZE_DIRECTORY': self.all_iter_size}
            json.dump(iter_dict, f_write, indent=2, separators=(',', ':'), ensure_ascii=False)
        with open(self.pos_pickle, 'wb') as f:
            pickle.dump(iter_dict, f)
        res = pickle.dumps(self.my_dict_list, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


if __name__ == '__main__':
    name_dir = 'C:\\PycharmProjects\\homework_GB\\homework_7'
    name_csv = 'test_csv.CSV'
    name_json = 'test_json.json'
    name_pickle = 'test_pickle.pickle'
    obj_one = Write_inf_dir(name_dir, name_csv, name_json, name_pickle)
    obj_one.write_file()
