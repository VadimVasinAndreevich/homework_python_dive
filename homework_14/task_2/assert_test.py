import os
import json
import pickle
import pytest


def write_inf_dir(path_iter, pos_csv, pos_json, pos_pickle):
    my_dict_list = []
    with open(pos_csv, 'w', newline='', encoding='utf-8') as f_write:
        f_write.write(f"'DIRECTORY_NAME','FILE_NAME','SIZE_FILE','SIZE_FILES_DIRECTORY','SIZE_DIRECTORY'\n")
        all_iter_size = 0
        for dir_path, dir_name, file_name in os.walk(path_iter):
            size_score = 0
            for el in file_name:
                size = os.path.getsize(f'{dir_path}\\{el}')
                size_score += size
                f_write.write(f"{dir_path},{el},{size}\n")
            f_write.write(f"{dir_path},False,False,{size_score}\n")
            all_iter_size += size_score
        f_write.write(f"{path_iter},False,False,False,{all_iter_size}\n")
    with open(pos_json, 'w', newline='', encoding='utf-8') as f_write:
        for dir_path, dir_name, file_name in os.walk(path_iter):
            size_score = 0
            for el in file_name:
                size = os.path.getsize(f'{dir_path}\\{el}')
                size_score += size
            my_dict = {
                dir_path: {k: os.path.getsize(f'{dir_path}\\{k}') for k in file_name},
                'SIZE_FILES_DIRECTORY': size_score,
            }
            my_dict_list.append(my_dict)
        iter_dict = {path_iter: my_dict_list, 'SIZE_DIRECTORY': all_iter_size}
        json.dump(iter_dict, f_write, indent=2, separators=(',', ':'), ensure_ascii=False)
    with open(pos_pickle, 'wb') as f:
        pickle.dump(iter_dict, f)
    res = pickle.dumps(my_dict_list, protocol=pickle.DEFAULT_PROTOCOL)
    print(f'{res = }')


def test_string():
    for el in [name_dir, name_csv, name_json, name_pickle]:
        assert type(el) == str, f'проверьте на строковый тип: {el}'


def test_form_csv():
    test_csv = name_csv.split('.')
    assert test_csv[1] == 'CSV', 'формат должен быть - CSV'


def test_form_json():
    test_json = name_json.split('.')
    assert test_json[1] == 'json', 'формат должен быть - json'


def test_form_pickle():
    test_pickle = name_pickle.split('.')
    assert test_pickle[1] == 'pickle', 'формат должен быть - pickle'


def test_name_dir():
    assert name_dir[0:2] == 'C:', 'путь должен быть абсолютный'


name_dir = 'C:\\PycharmProjects\\homework_GB\\homework_7'
name_csv = 'test_csv.CSV'
name_json = 'test_json.json'
name_pickle = 'test_pickle.pickle'
write_inf_dir(name_dir, name_csv, name_json, name_pickle)


if __name__ == '__main__':
    pytest.main()
