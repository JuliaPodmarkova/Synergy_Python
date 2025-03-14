# Задача 3. Квадрат наибольшего числа

def max_square(*num):
    if not num:
        return None
    max_num = max(num)
    return max_num ** 2

print(max_square(3))
print(max_square(3, 7, 0, 1))
print(max_square(5, 3, 4, 9))
