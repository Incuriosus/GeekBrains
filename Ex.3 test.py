gen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gen_2 = iter(gen)
for _ in range(10):
    print(f'Цикл работает {_}-й раз')
    for idx in gen_2:
        print(f'Работает второй цикл, значение {idx}')
        break

