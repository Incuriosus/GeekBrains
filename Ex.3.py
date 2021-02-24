exception = ['11', '12', '13', '14']
for i in range(1000):
    percent = str(i)
    word = ' процент'
    if int(percent[-1]) == 0 or percent[-2:len(percent)] in exception or int(percent[-1]) >= 5:
        word += 'ов'
    elif 1 < int(percent[-1]) < 5:
        word += 'а'
    print(percent + word)
