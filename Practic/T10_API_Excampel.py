# Пример работы с API

import requests
timezone = 'Europe/Moscow'
api_url = 'https://api.api-ninjas.com/v1/worldtime?timezone={}'.format(timezone)
response = requests.get(api_url, headers={'X-Api-Key': 'I3b6IFmrQq0NS**********wKhrFwwUu9k'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
response.json()



