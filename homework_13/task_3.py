import os
import json
import pickle
from Test import Protect_str, Protect_form, Protect_write


class Write_inf_dir:
    my_dict_list = []
    all_iter_size = 0

    def __init__(self, path_iter, pos_csv, pos_json, pos_pickle):
        if not isinstance(path_iter, str) or not isinstance(pos_csv, str) or not isinstance(pos_json, str)\
                or not isinstance(pos_pickle, str):
            raise Protect_str(path_iter, pos_csv, pos_json, pos_pickle)
        if '\\' not in path_iter or '.' not in pos_csv or '.' not in pos_json or '.' not in pos_pickle:
            raise Protect_write(path_iter, pos_csv, pos_json, pos_pickle)
        if pos_csv[pos_csv.index('.')+1:len(pos_csv)] != 'CSV' or \
                pos_json[pos_json.index('.')+1:len(pos_json)] != 'json' or \
                pos_pickle[pos_pickle.index('.')+1:len(pos_pickle)] != 'pickle':
            raise Protect_form(pos_csv, pos_json, pos_pickle)
        else:
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
