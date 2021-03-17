with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        with open('users_hobby.txt', 'w', encoding='utf-8') as users_hobby:
            n1 = "\n"
            for line in users:
                hobby_counter = hobby.readline()
                if hobby_counter:
                    users_hobby.write(f'{line.replace(n1, "")}: {hobby_counter}')
                else:
                    users_hobby.write(f'{line.replace(n1, "")}: None{n1}')
            if hobby.readline():
                raise SystemExit(1)
