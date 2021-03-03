import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, joke_nouns=nouns, joke_adverbs=adverbs, joke_adjectives=adjectives, repeat=True):
    """Создает шутку из трех явно заданных списков слов"""
    result = []
    if repeat:
        for i in range(num):
            result.append(f'{random.choice(joke_nouns)} {random.choice(joke_adverbs)} {random.choice(joke_adjectives)}')
        return result
    else:
        random.shuffle(joke_nouns)
        random.shuffle(joke_adverbs)
        random.shuffle(joke_adjectives)
        for noun, adverb, adjective in zip(joke_nouns, joke_adverbs, joke_adjectives):
            result.append(f'{noun} {adverb} {adjective}')
        return result[0:num]


print(get_jokes(9))
print(get_jokes(3, repeat=False))
