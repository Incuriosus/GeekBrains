# Скрипт для записи данных
import sys


def add_sale(sale):
    with open('bakery.csv', 'a', encoding='utf-8') as bakery:
        bakery.write(sale + '\n')


if __name__ == '__main__':
    add_sale(sys.argv[1])
