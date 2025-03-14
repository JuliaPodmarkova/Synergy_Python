# Задача 1. Вычисление степени без цикла

def power(n, m):
    if m == 0:
        return 1
    elif m < 0:
        return None
    else:
        return n * power(n, m - 1)

print(power(2, 3))
print(power(2, 0))
print(power(5, 3))
