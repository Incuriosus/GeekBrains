prices = [57.8, 46.51, 97, 13.2, 18.34, 24, 69.92, 37.3, 19.21, 7.14, 2, 81.45, 95, 14.67, 57.2]
# A Вывести на экран эти цены через запятую в одну строку
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
messege = []
for price in prices:
    price_str = f'{price:.2f}'
    rub = price_str.split('.')[0]
    kop = price_str.split('.')[1]
    # обе переменные можно прописать сразу в формат строке, но так, вроде, сложнее читается.
    messege.append(f'{rub} руб {kop} коп')
print(', '.join(messege))
print(id(messege))
print(id(prices))

# B Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

prices.sort()
messege.clear()
for price in prices:
    price_str = f'{price:.2f}'
    rub = price_str.split('.')[0]
    kop = price_str.split('.')[1]
    messege.append(f'{rub} руб {kop} коп')
print(', '.join(messege))
print(id(messege))
print(id(prices))

# C Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices_rev = prices[::-1]

# D Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print(', '.join(messege[-5:]))