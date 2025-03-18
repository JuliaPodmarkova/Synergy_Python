# Задача 2. По следам четных чисел: Количество четных чисел во вложенных списках

def count_even_numbers(list1):
    count = 0

    for i in list1:
        if isinstance(i, list):
            count += count_even_numbers(i)
        elif isinstance(i, int) and i % 2 == 0:
            count += 1

    return count

a = [1, 2, [3, 4, [5, 6]], 7, [8]]
b = [1, [2, [3, [4, [5, [6, [7, [8, [9, [0]]]]]]]]]]
c = [1, 2, 3.14, 4, 5, 6, 7 ]

even_a = count_even_numbers(a)
even_b = count_even_numbers(b)
even_c = count_even_numbers(c)

print(even_a)
print(even_b)
print(even_c)
