# Задача 1. Автомат с газировкой

v = float(input('Введите первоначальный объем газировки в литрах: '))

while v >= 0.2:
    print('OK')
    v = v - 0.2
    continue
else:
    print('Error: lack of water!')

