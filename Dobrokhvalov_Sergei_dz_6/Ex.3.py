import json

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbys:
        with open('users_hobby.json', 'w', encoding='utf-8') as users_hobby:
            users_hobby_content = {}
            user_content = users.read().splitlines()
            hobby_content = hobbys.read().splitlines()
            if len(user_content) < len(hobby_content):
                raise SystemExit(1)
            else:
                for idx in range(len(user_content) - len(hobby_content)):
                    hobby_content.append(None)
                for user, hobby in zip(user_content, hobby_content):
                    users_hobby_content[user] = hobby
            users_hobby.write(json.dumps(users_hobby_content))

with open('users_hobby.json', 'r', encoding='utf-8') as users_hobby:
    users_hobby_con = json.loads(users_hobby.read())
    print(users_hobby_con)
