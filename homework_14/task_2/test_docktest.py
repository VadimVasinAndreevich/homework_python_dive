import os
import json
import pickle


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


def is_prime(*args):
    """
    >>> is_prime('C:\\PycharmProjects\\homework_GB\\homework_7', \
    'test_csv.CSV', 'test_json.json', 'test_pickle.pickle')
    True
    """
    for el in args:
        if not isinstance(el, str):
            raise TypeError('тип объекта должен быть - строка')
    for el in [args[1], args[2], args[3]]:
        if '.' not in el:
            raise ValueError('в строке не указан формат файла')
    if 'C:' not in args[0][0:2]:
        raise ValueError('путь к директории не является абсолютным')
    name_dir = args[0]
    name_csv = args[1]
    name_json = args[2]
    name_pickle = args[3]
    write_inf_dir(name_dir, name_csv, name_json, name_pickle)
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
