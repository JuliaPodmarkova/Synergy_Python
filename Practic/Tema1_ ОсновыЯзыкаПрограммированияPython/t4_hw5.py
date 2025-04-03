# Задача 5. Порядочные списки

num_of_list_1, num_of_list_2 = int(input('Введите количество элементов списка №1: ')), int(input('Введите количество элементов списка №2: '))
list_1 = []
list_2 = []
list_3 = []

while num_of_list_1 > 0:
    numbers_list_1 = [int(input('Введите число для списка №1: '))]
    num_of_list_1 -= 1
    for num_1 in numbers_list_1:
        list_1.append(num_1)
        continue

while num_of_list_2 > 0:
    numbers_list_2 = [int(input('Введите число для списка №2: '))]
    num_of_list_2 -= 1
    for num_2 in numbers_list_2:
        list_2.append(num_2)
        continue
else:
    list_3 = list_1 + list_2
    print(sorted(list_3))


