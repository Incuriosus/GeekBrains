def val_checker(check_arg):
    def _val_checker(callback):
        def wrapper(arg):
            try:
                if check_arg(arg):
                    return callback(arg)
                else:
                    raise ValueError
            except ValueError:
                print(f'ValueError: wrong val {arg}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(-5))


