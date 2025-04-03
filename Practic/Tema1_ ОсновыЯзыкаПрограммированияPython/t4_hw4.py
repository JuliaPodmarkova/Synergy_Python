# Задача 4. Странный регулировщик

quantity_automobils = int(input('Введите количество автомобилей подъехавших к перекрестку: '))
right = []
left = []
while quantity_automobils > 0:
    numbers_of_automobils = [int(input('Введите номер автомобиля: '))]
    quantity_automobils -= 1
    for num in numbers_of_automobils:
        if num % 2 == 0:
            right.append(num)
            continue
        elif num % 2 != 0:
            left.append(num)
            continue
else:
    print(sorted(right))
    print(sorted(left, reverse = True))

