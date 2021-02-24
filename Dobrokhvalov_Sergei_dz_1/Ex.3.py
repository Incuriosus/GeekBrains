exception = [11, 12, 13, 14]
for i in range(1000):
    percent = i
    word = ' процент'
    if percent % 10 == 0 or percent % 100 in exception or percent % 10 >= 5:
        word += 'ов'
    elif 1 < percent % 10 < 5:
        word += 'а'
    print(str(percent) + word)
