import random
import timeit

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    n = 5
    fib_result = fibonacci(n)
    print('------------------------------------------------------------------------')
    print()
    print(f"Число Фибоначчи для n={n}: {fib_result}")
    print('------------------------------------------------------------------------')
    print()
    print('Анализ стека вызовов для n = 5:\n'
          'Когда мы вызываем fibonacci(5), стек вызовов будет выглядеть следующим образом:\n'
          'fibonacci(5)\n'
          '  -> fibonacci(4)\n'
          '   -> fibonacci(3)\n'
          '    -> fibonacci(2)\n'
          '     -> fibonacci(1) # возвращает 1\n'
          '      -> fibonacci(0) # возвращает 0\n'
          '   # возвращает 1 + 0 = 1\n'
          '   -> fibonacci(1) # возвращает 1\n'
          '  # возвращает 1 + 1 = 2\n'
          '  -> fibonacci(2)\n'
          '   -> fibonacci(1)  # возвращает 1\n'
          '    -> fibonacci(0)  # возвращает 0\n'
          '  # возвращает 1 + 0 = 1\n'
          '  # возвращает 2 + 1 = 3\n'
          '  -> fibonacci(3)\n'
          '   -> fibonacci(2)\n'
          '    -> fibonacci(1)  # возвращает 1\n'
          '     -> fibonacci(0)  # возвращает 0\n'
          '  # возвращает 1 + 0 = 1\n'
          '  -> fibonacci(1)  # возвращает 1\n'
          '  # возвращает 1 + 1 = 2\n'
          '# возвращает 3 + 2 = 5')

    print('------------------------------------------------------------------------')
    print()
    sample_list = [random.randint(0, 100) for _ in range(10)]
    max_element = find_max(sample_list)
    print(f"Список: {sample_list}, Максимальный элемент в списке: {max_element}")
    print('------------------------------------------------------------------------')
    print()

    lengths = [10, 100, 1000]
    for length in lengths:
        random_list = [random.randint(0, 1000) for _ in range(length)]

        print(f"\nСписок длиной {length}:")

        quicksort_time = timeit.timeit('quicksort(random_list)', globals=globals(), number=100)
        print(f'Список: {random_list}')
        print(f'Остортированный список (быстрая сортировка): {quicksort(random_list)}')
        print(f"Время быстрой сортировки: {quicksort_time:.6f} секунд")

        insertion_sort_time = timeit.timeit('insertion_sort(random_list)', globals=globals(), number=100)
        print(f'Остортированный список (сортировка вставками): {insertion_sort(random_list)}')
        print(f"Время сортировки вставками: {insertion_sort_time:.6f} секунд")
        print('------------------------------------------------------------------------')
        print()