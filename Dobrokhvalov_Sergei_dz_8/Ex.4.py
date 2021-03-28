def val_checker(check_arg):
    def _val_checker(callback):
        def wrapper(arg):
            if check_arg(arg):
                return callback(arg)
            else:
                raise ValueError

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    a = -5
    try:
        print(calc_cube(a))
    except ValueError:
        print(f'ValueError: wrong val {a}')
