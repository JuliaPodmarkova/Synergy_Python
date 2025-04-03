# Задача 1. Анализ данных о космических кораблях

import csv

with open('spaceships.csv', mode='r', encoding='utf-8', newline = '') as file:
    reader = csv.reader(file)
    header = next(reader)
    spaceships = [row for row in reader]

total_spaceships = len(spaceships)
print('Общее количество кораблей: ', total_spaceships)

ships_after_2000 = sum(1 for ship in spaceships if int(ship[2]) > 2000)
print('Количество кораблей, запущенных после 2000 года: ',ships_after_2000)

max_speed_ship = max(spaceships, key=lambda ship: int(ship[3]))
max_speed_name = max_speed_ship[0]
max_speed_country = max_speed_ship[4]
print('Корабль с максимальной скоростью: ', max_speed_name, '-', max_speed_country)
