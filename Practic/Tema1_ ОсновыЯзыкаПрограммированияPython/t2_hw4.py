# Задача 4. Треугольный вопрос
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число с: "))

if a == b == c:
    print('Равносторонний треугольник')
elif (a == b or a == c or b == c) and (a != b or a != c or b != c):
    print('Равнобедренный треугольник')
elif a + b > c and a + c > b and c + b > a:
    print('Обычный треугольник')
else:
    print("Ошибка")
