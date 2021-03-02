def thesaurus(*args):
    names_dict = {}
    for arg in args:
        if arg[0] in names_dict:
            names_dict.get(arg[0]).append(arg)
        else:
            names_dict[arg[0]] = []
            names_dict[arg[0]].append(arg)
    return names_dict

print(thesaurus('Петр', 'Мария', 'Сергей', 'Станислав', 'Андрей', 'Евгений', 'Анна'))
