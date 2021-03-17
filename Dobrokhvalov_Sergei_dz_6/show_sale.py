# Скрипт для демонстрации данных.
# Запуск скрипта выводит данные, запуск с параметром - выводит записи с указанного номера
# С двуми параметрами - от и до
import sys


def show_sale(*args):
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        if not args:
            for line in bakery:
                print(line.strip())
        elif len(args) == 1:
            counter = int(args[0]) - 1
            for line in bakery:
                if counter != 0:
                    counter -= 1
                    continue
                else:
                    print(line.strip())
        elif len(args) == 2 and int(args[1]) > int(args[0]):
            min_counter = int(args[0]) - 1
            max_counter = int(args[1]) - min_counter
            for line in bakery:
                if min_counter != 0:
                    min_counter -= 1
                    continue
                elif max_counter != 0:
                    print(line.strip())
                    max_counter -= 1
                else:
                    break
        else:
            print('Введены некорректные параметры')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        show_sale()
    else:
        show_sale(*sys.argv[1:])
