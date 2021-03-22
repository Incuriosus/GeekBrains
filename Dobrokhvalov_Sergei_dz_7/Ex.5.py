import os
import json


def scan_files(path='./'):
    summary = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            file_ex = os.path.basename(file).split('.')[-1]
            if 10**len(str(file_size)) not in summary:
                summary[10**len(str(file_size))] = [1, set()]
            else:
                summary[10**len(str(file_size))][0] += 1
            summary[10**len(str(file_size))][1].add(file_ex)
    for key in summary:
        summary[key][1] = list(summary[key][1])
        summary[key] = tuple(summary[key])
    return os.path.abspath(path), summary


if __name__ == '__main__':
    file_path, result = scan_files()
    file_name = f'{os.path.split(file_path)[1]}_summery.json'
    try:
        with open(f'{file_name}', 'w', encoding='utf-8') as f:
            json.dump(result, f)
    except FileExistsError as e:
        print(f'Нельзя сотворить здесь ({e})')
