import os
import json

with open('config.json', 'r', encoding='utf-8') as config:
    config_dict = json.load(config)


def mk_project(project_dict, path='./'):
    for key in project_dict:
        if '.' not in key:
            dir_path = os.path.join(path, key)
            os.mkdir(dir_path)
            mk_project(project_dict[key], dir_path)
        else:
            file_path = os.path.join(path, key)
            with open(file_path, 'a', encoding='utf-8') as key_file:
                continue


if __name__ == '__main__':
    try:
        mk_project(config_dict)
    except FileExistsError as e:
        print(f'Нельзя сотворить здесь ({e})')
