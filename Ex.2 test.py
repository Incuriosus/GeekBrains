words = {
    'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
    'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
    'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
}

# random.shuffle(nouns)
zipped = zip(*words.values())
print(list(zipped))

a = ['Петр Иванов', 'Мария Федотова', 'Сергей Абрамов', 'Станислав Горбунов', 'Андрей Коломийцев',
                    'Евгений Ройзман', 'Анна Каренина', 'Иван Аскеров']

a.sort()
print(a)
