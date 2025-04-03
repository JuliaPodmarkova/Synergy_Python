# Задача 3. Арифметическая прогрессия

def progression(first_element, step):
    def next_element():
        nonlocal first_element
        current_element = first_element
        first_element += step
        return current_element
    return next_element

f = progression(3, 5)
print(f())
print(f())
print(f())

print()

f = progression(12, -7)
print(f())
print(f())
print(f())
print(f())

print()
f = progression(6, 0)
print(f())
print(f())
print(f())
