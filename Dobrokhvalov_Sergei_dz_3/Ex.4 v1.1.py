def thesaurus_adv(*args):
    sort_list = []
    all_names_dict = {}
    for arg in args:
        sep_arg = arg.split()
        sort_list.append(sep_arg[1][0])
    sort_list.sort()
    for letter in sort_list:
        all_names_dict[letter] = {}
    list_args = list(args)
    list_args.sort()
    for arg in list_args:
        sep_arg = arg.split()
        fn_word = sep_arg[0][0]  # first name word
        ln_word = sep_arg[1][0]  # last name word
        if fn_word not in all_names_dict[ln_word]:
            all_names_dict[ln_word][fn_word] = []
        all_names_dict[ln_word][fn_word].append(arg)
    return all_names_dict


print(thesaurus_adv('Петр Иванов', 'Мария Федотова', 'Сергей Абрамов', 'Станислав Горбунов', 'Андрей Коломийцев',
                    'Евгений Ройзман', 'Анна Каренина', 'Иван Аскеров'))
