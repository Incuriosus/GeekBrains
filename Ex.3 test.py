tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Николай', 'Олег']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def tutor_gen():
    if len(tutors) > len(klasses):
        for idx in range(len(tutors) - len(klasses)):
            klasses.append(None)
    for tut, klas in zip(tutors, klasses):
        yield tut, klas


print(type(tutor_gen()))
res_gen = tutor_gen()
for idx in range(len(tutors)):
    print(next(res_gen))
print(next(res_gen))  # Истощение