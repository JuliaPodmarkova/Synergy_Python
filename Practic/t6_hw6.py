# Задача 6. Фруктам нужен порядок

fructs = ["orange", "grape", "strawberry", "banana", "kiwi"]

def bubble_sort_by_length(strings):
    n = len(strings)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
                swapped = True
        print(f"После прохода {i + 1}: {strings}")
        if not swapped:
            break
print("Исходный список:", fructs)
print()

bubble_sort_by_length(fructs)

print()
print("Отсортированный список:", fructs)

