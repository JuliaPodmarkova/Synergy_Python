# Задача 1. Подсчет гласных букв

import requests

def get_wikipedia_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return requests.RequestException(f'Ошибка при получении страницы. Статус код: {response.status_code}')

print(get_wikipedia_content('https://ru.wikipedia.org/wiki/Python'))