# Задача 1.Фильтр конвейера с батончиками
good_candy = []

while True:
    candy_bars = [int(input('Введите вес батончика в граммах: '))]
    for candy_bar in candy_bars:
        if candy_bar >= 40 and candy_bar <= 50:
            good_candy.append(candy_bar)
            continue
        elif candy_bar == 0:
            print(good_candy)
            break

