# Задача 3. Список уникальных цифр числа

number = (input('Введите целое число: '))
numbers = set()
for i in number:
    numbers.add(i)
print(sorted(numbers))
