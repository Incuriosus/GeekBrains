import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=True):
    result = []
    if repeat:
        for i in range(n):
            result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        return result
    else:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
            result.append(f'{noun} {adverb} {adjective}')
        return result[0:n]


print(get_jokes(5, repeat=False))
