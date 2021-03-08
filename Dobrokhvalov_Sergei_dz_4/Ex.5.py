# cli
import utils
import sys


def main(args):
    if not args:
        return 1
    elif len(args) == 1:
        print('Код валюты не был введен')
        return 0
    elif utils.currency_rates(args[1]):
        print(utils.currency_rates(args[1])[0], utils.currency_rates(args[1])[1])
        return 0
    print('Неверный аргумент')
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
