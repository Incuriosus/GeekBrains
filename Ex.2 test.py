numbers = [1, 2, 3, 4, 5, 6, 7, 8, 14, 23, 24, 25, 27, 28, 115]
all_summ = 0
for number in numbers:
    numbers_summ = 0
    for i in range(len(str(number))):
        numbers_summ += int(str(number)[i])
    if numbers_summ % 7 == 0:
        all_summ += number

# Тест тест тест

print(all_summ)