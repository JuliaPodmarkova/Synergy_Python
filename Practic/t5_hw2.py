# Задача 2. Маркировка батончиков

status_candy_bar_Ok = 'GOOD'
status_candy_bar_bad = 'BAD'
i = 0
j = 0
n = 0
candy_bar_dict = {}

summa_candy_bar = int(input('Введите количество маркируемых батончиков: '))

while summa_candy_bar > 0:
    candy_bar = input('Введите id батончика и его вес через пробел: ').split()
    summa_candy_bar -= 1
    if int(candy_bar[1]) >= 40 and int(candy_bar[1]) <= 50:
            i = status_candy_bar_Ok
            n = candy_bar[0]
            candy_bar_dict[n] = i
            continue
    elif int(candy_bar[1]) < 40 or int(candy_bar[1]) > 50:
            j = status_candy_bar_bad
            n = candy_bar[0]
            candy_bar_dict[n] = j
            continue
print(candy_bar_dict)

