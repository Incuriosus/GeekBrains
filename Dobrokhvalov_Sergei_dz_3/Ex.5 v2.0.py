import random
words = {
    'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
    'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
    'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"],
    #  'conjunctions': ["а", "и", "но", "да", "или"],
    #  'nouns_2': ["самолет", "поселок", "двор", "забор", "переулок"],
    #  'adjectives_2': ["грустный", "блеклый", "красный", "антиутопичный", "жесткий"]
}


def get_jokes(num, word_dict=words, repeat=True):
    """Создает шутку из словаря"""
    result = []
    if repeat:
        for i in range(num):
            joke = []
            for key in word_dict:
                joke.append(random.choice(word_dict.get(key)))
            result.append(" ".join(joke))
        return result
    else:
        for key in word_dict:
            random.shuffle(word_dict.get(key))
        for jokes in zip(*word_dict.values()):
            result.append(" ".join(list(jokes)))
        return result[0:num]


print(get_jokes(9))
print(get_jokes(3, repeat=False))
