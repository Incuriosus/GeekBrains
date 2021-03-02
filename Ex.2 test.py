import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# random.shuffle(nouns)
zipped = zip(nouns, adverbs, adjectives)
print(list(zipped))

# result = list(zip(list(map(random.shuffle, nouns))), list(map(random.shuffle, adverbs)), list(map(random.shuffle, adjectives))