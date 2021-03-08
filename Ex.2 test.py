from requests import get
import decimal
import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
response_list = response.content.decode(encoding=response.encoding)
print(response_list)
print(response_list.split('<CharCode>'))
currency = {}
for idx in range(1, len(response_list.split('<CharCode>'))):
    currency[response_list.split('<CharCode>')[idx][0:3]] = \
        response_list.split('<CharCode>')[idx].split('Value')[1][1:-2]
print(currency)
date_list = response_list.split('<CharCode>')[0].split('Date="')[1][:10].split('.')
print(date_list)
date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
print(date)
a = [decimal.Decimal('8.8'), date]
print(a[0])