# Задача 4. Генератор


def process_table_data(input_string):
    rows = input_string.strip().split('\n')

    final_result = []

    for row in rows:
        numbers = list(map(int, row.split(', ')))
        even_numbers = [x for x in numbers if x % 2 == 0]

        if even_numbers:
            squares = [x**2 for x in even_numbers]
            total_sum = sum(even_numbers)
            final_result.append(squares + [total_sum])
    return final_result

input_data = ""
for _ in range(3):
    input_data += input("Введите данные таблицы (числа в строках разделены запятой с пробелом ', '):\n") + '\n'

output = process_table_data(input_data)

print("Результат: ", output)
