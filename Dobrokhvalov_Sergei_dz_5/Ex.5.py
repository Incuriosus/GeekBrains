src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
rep_set = set()
uniq_set = set()
for number in src:
    if number in rep_set:
        continue
    if number in uniq_set:
        rep_set.add(number)
        uniq_set.discard(number)
        continue
    uniq_set.add(number)
for number in src:
    if number in uniq_set:
        result.append(number)
print(result)
