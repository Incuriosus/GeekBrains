def thesaurus_adv(*args):
    all_names_dict = {}
    for arg in args:
        sep_arg = arg.split()
        if 1 >= len(sep_arg) or len(sep_arg) >= 3:  # Если в списке приходит только имя или ФИО и т.п.
            continue
        else:
            fn_word = sep_arg[0][0]  # first name word
            ln_word = sep_arg[1][0]  # last name word
            if ln_word not in all_names_dict:
                all_names_dict[ln_word] = {}
                all_names_dict[ln_word][fn_word] = []
            else:
                if fn_word not in all_names_dict[ln_word]:
                    all_names_dict[ln_word][fn_word] = []
            all_names_dict[ln_word][fn_word].append(arg)
    return all_names_dict


print(thesaurus_adv('Петр Иванов', 'Мария Федотова', 'Сергей Абрамов', 'Станислав Горбунов', 'Андрей Коломийцев',
                    'Евгений Ройзман', 'Анна Каренина', 'Иван Аскеров', 'Артем Викторович Плющеев', 'Игнатий'))
