# Задача 4. Самая популярная цифра

number_of_digits = int(input('Введите количество чисел: '))
numbers = []
a = 0
while number_of_digits > 0:
    digit = (input('Введите число: '))
    number_of_digits -= 1
    for i in digit:
        numbers.append(i)
print(max((numbers), key=numbers.count))
