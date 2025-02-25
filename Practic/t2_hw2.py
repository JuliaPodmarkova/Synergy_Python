# Задача 2. Сортировка по параметрам
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
s = input("Введите символ < или >")
if s == ">":
    if a > b:
        print(a, b)
    else:
        print(b, a)
else:
    if a > b:
        print(b, a)
    else:
        print(a, b)
