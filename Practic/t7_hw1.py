# Задача 1. Високосный год

def year_is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 'LEAP'
    else:
        return 'IS NOT LEAP'

print(year_is_leap(2003))
print(year_is_leap(2004))
print(year_is_leap(2000))
