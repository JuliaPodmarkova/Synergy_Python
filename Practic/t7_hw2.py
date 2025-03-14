# Задача 2. Неравенство треугольника

def triangle_exists(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b):
        return True
    else:
        return False

print(triangle_exists(2, 3, 4))
print(triangle_exists(2, 3, 5))
print(triangle_exists(2, 3, 6))
