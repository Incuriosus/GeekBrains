sent = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(sent):
    if str(sent[i]).isdigit():
        sent[i] = f'{int(sent[i]):02d}'
        sent.insert(i, '"')
        sent.insert(i+2, '"')
        i += 3
    else:
        if str(sent[i])[1:].isdigit():
            sent[i] = f'{sent[i][:1]}{int(sent[i][1:]):02d}'
            sent.insert(i, '"')
            sent.insert(i + 2, '"')
            i += 3
    i += 1

print(sent)

for i in range(len(sent)):
    if str(sent[i]).isdigit():
        sent[i] = "".join(sent[i-1:i+2])
    else:
        if str(sent[i])[1:].isdigit():
            sent[i] = "".join(sent[i - 1:i + 2])

for i in range(sent.count('"')):
    sent.remove('"')

print(' '.join(sent))
