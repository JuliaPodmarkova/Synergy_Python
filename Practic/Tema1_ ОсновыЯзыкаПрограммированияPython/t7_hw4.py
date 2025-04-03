# Задача 4. Очень четные элементы

def very_even(numbers):
    return [num for index, num in enumerate(numbers) if index % 2 == 1 and num % 2 == 0]

print(very_even([2, 3, 4, 11, 3,  6, -4, 0]))
print(very_even([]))
print(very_even([2, 1]))
