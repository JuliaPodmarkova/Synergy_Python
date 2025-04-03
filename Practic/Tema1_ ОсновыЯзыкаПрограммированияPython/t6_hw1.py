# Задача 1. Квадратный стиль

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for num in list:
    if num % 2 == 0:
        my_list.append(num ** 2)
print(my_list)
