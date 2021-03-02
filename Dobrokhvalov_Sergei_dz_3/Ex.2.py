numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(word, word_dict=numbers):
    if word.islower():
        print(word_dict.get(word))
    else:
        print(word_dict.get(word.lower()).title())


num_translate_adv(input('Введите число от нуля до десяти на английском:'))
