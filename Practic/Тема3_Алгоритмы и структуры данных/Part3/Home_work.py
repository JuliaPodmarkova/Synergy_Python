import random
import timeit
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]

def compare_sorting_algorithms(sizes):
    bubble_times = []
    insertion_times = []
    selection_times = []

    for size in sizes:
        random_list = generate_random_list(size)
        print(f"\nСозданный список ({size} элементов): {random_list}")

        bubble_time = timeit.timeit('bubble_sort(arr)', globals={'bubble_sort': bubble_sort, 'arr': random_list.copy()}, number=10)
        bubble_times.append(bubble_time / 10)  # Среднее время
        sorted_bubble = bubble_sort(random_list.copy())
        print(f"Результат пузырьковой сортировки: {sorted_bubble},\nВремя (среднее): {bubble_time / 10:.5f} сек")

        insertion_time = timeit.timeit('insertion_sort(arr)', globals={'insertion_sort': insertion_sort, 'arr': random_list.copy()}, number=10)
        insertion_times.append(insertion_time / 10)  # Среднее время
        sorted_insertion = insertion_sort(random_list.copy())
        print(f"Результат сортировки вставками: {sorted_insertion},\nВремя (среднее): {insertion_time / 10:.5f} сек")

        selection_time = timeit.timeit('selection_sort(arr)', globals={'selection_sort': selection_sort, 'arr': random_list.copy()}, number=10)
        selection_times.append(selection_time / 10)  # Среднее время
        sorted_selection = selection_sort(random_list.copy())
        print(f"Результат сортировки выбором: {sorted_selection},\nВремя (среднее): {selection_time / 10:.5f} сек")
        print("-" * 80)
    return bubble_times, insertion_times, selection_times

def plot_comparison(sizes, bubble_times, insertion_times, selection_times):
    plt.plot(sizes, bubble_times, label='Пузырьковая сортировка', color='red', marker='o')
    plt.plot(sizes, insertion_times, label='Сортировка вставками', color='blue', marker='o')
    plt.plot(sizes, selection_times, label='Сортировка выбором', color='green', marker='o')

    plt.xlabel('Размер списка')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени выполнения алгоритмов сортировки')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    sizes = [100, 200, 300, 400, 500]  # Размеры списков для тестирования
    bubble_times, insertion_times, selection_times = compare_sorting_algorithms(sizes)
    plot_comparison(sizes, bubble_times, insertion_times, selection_times)