numbers = []
all_summ = 0
for i in range(1000):
    if i % 2 != 0:
        numbers.append(i**3)

print(numbers)

for number in numbers:
    numbers_summ = 0
    for i in range(len(str(number))):
        numbers_summ += int(str(number)[i])
    if numbers_summ % 7 == 0:
        all_summ += number

print(all_summ)

for i in range(len(numbers)):
    numbers[i] = numbers[i] + 17
    
print(numbers)

all_summ = 0

for number in numbers:
    numbers_summ = 0
    for i in range(len(str(number))):
        numbers_summ += int(str(number)[i])
    if numbers_summ % 7 == 0:
        all_summ += number

print(all_summ)

