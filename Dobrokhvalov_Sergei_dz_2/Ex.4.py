prices = [57.8, 46.51, 97, 13.2, 18.34, 24, 69.92, 37.3, 19.21, 7.14, 2, 81.45, 95, 14.67, 57.2]

# A Вывести на экран эти цены через запятую в одну строку
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
messege = []
for price in prices:
    if "." in str(price):
        rub = str(price).split('.')[0]
        kop = str(price).split('.')[1] # Если 0.8 он выводит 8 копеек
        messege.append(f'{rub} руб {int(kop):02d} коп')
    else:
        messege.append(f'{price} руб 00 коп')
print(', '.join(messege))

print(prices)
print(id(prices))

# B Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

messege = []
for price in prices:
    if "." in str(price):
        rub = str(price).split('.')[0]
        kop = str(price).split('.')[1]
        messege.append(f'{rub} руб {int(kop):02d} коп')
    else:
        messege.append(f'{price} руб 00 коп')
print(', '.join(messege))

print(prices)
print(id(prices))

# C Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices_rev = prices[::-1]
print(prices_rev)

# D Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


# Как работает сорт с перезаписанным списком?
# Можно ли настроить вывод в строку не изменяя список?

