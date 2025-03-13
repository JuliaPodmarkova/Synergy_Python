# Задача 3. Буквы любят цифры

str_1 = input('Введите строку: ')
str1 = str_1.split(', ')
integers = []
length = len(str1)
i = 0
list1 = []
even = 0

#Вычлиняем цифры(числа) из строки
while i < length:
    str1_int = ''
    while i < length and '0' <= str1[i] <= '9':
        str1_int += str1[i]
        i += 1
    i += 1
    if str1_int != '':
        integers.append(int(str1_int))

#Вычисляем количество четных чисел
for num in integers:
    if num % 2 == 0:
        even += 1

#Выводим на печать новый список содержащие условия задачи,
#в зависимости от количество четных чисел в строке
if even >= 2:
    list1 = [i * i for i in integers if even >= 2]
    print(list1)
elif even < 2:
    print('-'.join(str1))




