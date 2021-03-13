def numbers_gen(n):
    numbers = (number for number in range(1, n+1, 2))
    return numbers


print(list(numbers_gen(15)))
