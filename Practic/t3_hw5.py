# Задача 5. Квадраты в диапазоне
import math

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a < 0:
        a = 0
        for i in range(a, b + 1, 1):
            if math.sqrt(i) % 1 == 0:
                print(i)
else:
    for i in range(a, b + 1, 1):
        if math.sqrt(i) % 1 == 0:
            print(i)
