# Задача 1. Получение текущего курса доллара

import requests

def curs():
    response = requests.get('https://www.cbr.ru/currency_base/daily/')
    if response.status_code == 200:
        index = response.text.find('Доллар США')
        index = response.text.find('<td>', index)
        index_end = response.text.find('</td>', index)
        dollar_rate = response.text[index + 4:index_end]
        return dollar_rate
    else:
        requests.RequestException("Ошибка при выполнении запроса")

print(f'Тукущий курс доллара: {curs()}')