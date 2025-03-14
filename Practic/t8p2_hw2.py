# Задача 2. Герератор квадратов

import datetime

def date_gen(start_date):
    current_date = datetime.date(*start_date)
    while True:
        yield (current_date.year, current_date.month, current_date.day)
        current_date += datetime.timedelta(days=1)

g = date_gen((2023, 10, 15))

print(next(g))
print(next(g))
print(next(g))

print()

g = date_gen((2023 , 11, 29))

print(next(g))
print(next(g))
print(next(g))
