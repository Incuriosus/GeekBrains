def type_logger(callback):

    def wrapper(*args, **kwargs):
        result_list = []
        for arg in args:
            result_list.append(f'{callback.__name__}({arg}: {type(arg)})')
        for kwarg in kwargs:
            result_list.append(f'{callback.__name__}({kwargs[kwarg]}: {type(kwarg)})')
        return ', '.join(result_list)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5, 4, name='Serj', password='12345'))
