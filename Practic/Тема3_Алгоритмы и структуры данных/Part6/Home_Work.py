import random
import timeit
import matplotlib.pyplot as plt

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Список пуст")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Список пуст")

def process_tasks(tasks):
    queue = Queue()
    current_time = 0

    for task in tasks:
        queue.enqueue(task)

    while not queue.is_empty():
        task = queue.dequeue()
        current_time += task['duration']
        print(f"Задача '{task['name']}' выполнена за время: {current_time} минут")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def time_sort(sort_function, arr):
    timer = timeit.Timer(lambda: sort_function(arr.copy()))
    return timer.timeit(number=10)

# Пример задач
tasks = [
    {'name': 'Изучить тех.задание', 'duration': 15},
    {'name': 'Создать программный код', 'duration': 30},
    {'name': 'Проверить получившийся код', 'duration': 5},

]

print("Задачи в процессе:")
print()
process_tasks(tasks)
print()
print("_____________________________________________________________________")

print("Сортировка слиянием: ")
print()
arr = []
for i in range(10):
    arr.append(random.randint(0, 10))
print("Список для сортировки", arr)
a = merge_sort(arr)
print("Отсортированный список: ", a)
print()
print("_____________________________________________________________________")

lengths = [10, 100, 1000]
merge_times = []
bubble_times = []
for length in lengths:
    test_array = [random.randint(0, 10000) for _ in range(length)]

    merge_time = time_sort(merge_sort, test_array)
    merge_times.append(merge_time)
    print(f"Сортировка слиянием для {length} элементов произведена за: {merge_time:.6f} секунд")

    bubble_time = time_sort(bubble_sort, test_array)
    bubble_times.append(bubble_time)
    bubble_time = time_sort(bubble_sort, test_array)
    print(f"Пузырьковая сортировка для {length} элементов произведена за: {bubble_time:.6f} секунд")
    print()
    print("_____________________________________________________________________")

plt.scatter([10, 100, 1000], [merge_times[0], merge_times[1], merge_times[2]], color='blue', s=100, zorder=5)
plt.scatter([10, 100, 1000], [bubble_times[0], bubble_times[1], bubble_times[2]], color='orange', s=100, zorder=5)
plt.figure(figsize=(10, 5))
plt.plot(lengths, merge_times, label='Сортировка слиянием', marker='o')
plt.plot(lengths, bubble_times, label='Пузырьковая сортировка', marker='o')
plt.title('Сравнение времени выполнения сортировок')
plt.xlabel('Количество элементов')
plt.ylabel('Время (секунды)')
plt.legend()
plt.grid()
plt.show()
