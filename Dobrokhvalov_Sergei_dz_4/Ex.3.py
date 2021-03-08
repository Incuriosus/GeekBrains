from requests import get
import decimal
import datetime


def currency_rates(code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_list = response.content.decode(encoding=response.encoding)
    currency = {}
    date_list = response_list.split('Date="')[1][:10].split('.')
    date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    for idx in range(1, len(response_list.split('<CharCode>'))):
        value = decimal.Decimal('.'.join(response_list.split('<CharCode>')[idx].split('Value')[1][1:-2].split(',')))
        currency[response_list.split('<CharCode>')[idx][0:3]] = [value, date]
    return currency.get(code.upper())


print(currency_rates('usd'))
print(currency_rates('Eur'))
