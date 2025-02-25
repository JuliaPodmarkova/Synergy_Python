# Задача 2.Возврат бракованных батончиков
bad_candy = []

while True:
    candy_bars = [int(input('Введите вес батончика в граммах: '))]
    for candy_bar in candy_bars:
        if candy_bar < 40 and candy_bar != 0 or candy_bar > 50:
            bad_candy.append(candy_bar)
            continue
        elif candy_bar == 0:
            print(sorted(bad_candy, reverse = False))
            break

