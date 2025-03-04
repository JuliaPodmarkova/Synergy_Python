# Задача 5. Два водителя
print('Введите маршруты водителей (города посещения через пробел).')
driver_1 = (input('Введите маршрут первого водителя: ')).split()
driver_2 = (input('Введите маршрут второго водителя: ')).split()
set1 = {0}
set2 = {0}
for city in driver_1:
    set1.add(city)
set1.remove(0)
for city in driver_2:
    set2.add(city)
set2.remove(0)
set3 = set1&set2
sorted(set3, reverse=False)
print(set3)
