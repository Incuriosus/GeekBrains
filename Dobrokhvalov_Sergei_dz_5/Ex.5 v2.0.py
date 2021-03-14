src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
all_num_set = set()
not_uniq_set = set()
for number in src:
    if number in all_num_set:
        not_uniq_set.add(number)
    all_num_set.add(number)
all_num_set -= not_uniq_set
for number in src:
    if number in all_num_set:
        result.append(number)
print(result)
