empls = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Вывести фразы вида "Привет, Игорь!"

for empl in empls:
    name = empl.split(' ')[-1].title()
    print(f'Привет, {name}!')