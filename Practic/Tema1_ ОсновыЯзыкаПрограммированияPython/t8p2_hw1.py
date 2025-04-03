# Задача 1. Генератор квадратов

def square_gen():
    n = 0
    while True:
        yield n ** 2
        n += 1

g = square_gen()

print(next(g))
print(next(g))
print(next(g))

print()

g = square_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
