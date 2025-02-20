# Задача 5. Камень, Ножницы, Бумага

print('Игра "Камень, ножницы, бумага"')
first_player = input("Первый игрок, введите или камень, или ножницы, или бумага: ").lower()
second_player = input("Второй игрок, введите или камень, или ножницы, или бумага: ").lower()
if first_player == 'камень':
    if second_player == 'камень':
        print('ничья')
    elif second_player == 'ножницы':
        print("победил первый игрок")
    elif second_player == 'бумага':
        print("победил второй игрок")
elif first_player == 'ножницы':
    if second_player == 'камень':
        print("победил второй игрок")
    elif second_player == 'ножницы':
        print('ничья')
    elif second_player == 'бумага':
        print("победил первый игрок")
elif first_player == 'бумага':
    if second_player == 'камень':
        print("победил первый игрок")
    elif second_player == 'ножницы':
        print("победил второй игрок")
    elif second_player == 'бумага':
        print('ничья')
else:
    print('Ошибка')
print('Спасибо за игру!')



