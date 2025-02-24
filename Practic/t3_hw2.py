# Задача 2. Счетчик бракованных батончиков

count = 0
bad_count = 0

while True:
    candy_bar = int(input('Введите вес батончика в граммах: '))
    if candy_bar >= 40 and candy_bar <= 50:
        count += 1
        print('GOOD')
        continue
    elif candy_bar != 0 and candy_bar < 40 or candy_bar > 50:
        bad_count += 1
        print('BAD')
        continue
    else:
        n = bad_count / (count + bad_count)
        print(f'{n:.2f}')
        break




