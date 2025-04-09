import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, num_target_l):
    for index, value in enumerate(arr):
        if value == num_target_l:
            return index
    return -1

def binary_search(arr, num_target_b):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == num_target_b:
            return mid
        elif arr[mid] < num_target_b:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print('Анализ временной и пространственной сложности бинарного поиска:\n 1. Временная сложность:\n'
      '- В лучшем случае O(1) - когда элемент находится в середине массива/списка\n'
      '- В среднем и худшем случае O(log n) - каждый раз делим массив пополам.\n'
      'Пространственная сложность O(1) - используется фиксированное количество переменных.')

random_numbers = sorted(random.sample(range(1, 1000), 100))
print(f'Список чисел: {random_numbers}')

search_values = [random_numbers[10], 500, random_numbers[-1], 1001]
print(f"Числа для поиска {search_values} и результаты их поиска: ")

for value in search_values:
    linear_index = linear_search(random_numbers, value)
    binary_index = binary_search(random_numbers, value)
    print(f"Поиск числа {value}: Линейный поиск -> индекс {linear_index},\nБинарный поиск -> индекс {binary_index}")

sizes = list(range(10, 1001, 10))
linear_times = []
binary_times = []

for size in sizes:
    test_list = sorted(random.sample(range(1, 1002), size))
    target = random.choice(test_list)

    start_time = time.time()
    linear_search(test_list, target)
    linear_times.append(time.time() - start_time)


    start_time = time.time()
    binary_search(test_list, target)
    binary_times.append(time.time() - start_time)
print(f'Время проведения линейного поиска на списке {test_list}:\n{linear_times}')
print(f'Время проведения бинарного поиска на списке {test_list}:\n{binary_times}')

plt.plot(sizes, linear_times, label='Линейный поиск', color='blue')
plt.plot(sizes, binary_times, label='Бинарный поиск', color='red')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (с)')
plt.title('Сравнение времени выполнения линейного и бинарного поиска')
plt.legend()
plt.grid()
plt.show()

print('Вывод: линейный поиск в среднем проводится в 2 раза дольше чем бинарный.')