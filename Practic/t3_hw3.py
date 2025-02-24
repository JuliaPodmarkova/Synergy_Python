# Задача 3. Star stair

'''star = int(input('Введите число: '))
for i in range(1, star + 1):
    print('*' * i)'''

stars = int(input('Введите число: '))
star = 1

while stars > 0:
    print('*' * star)
    star += 1
    stars -= 1


