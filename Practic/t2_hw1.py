# Задача 1. Сортировка трёх чисел
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число с: "))

if a < b:
    if b < c:
        print (a, b, c)
    else:
        if a < c:
            print (a, c, b)
        else:
            print (c, a, b)
else:
    if c < b:
        print (c, b, a)
    else:
        if c < a:
            print (b, c, a)
        else:
            print (b, a, c)
