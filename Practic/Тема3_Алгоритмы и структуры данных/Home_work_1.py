import random
import timeit
import matplotlib.pyplot as plt

# 01. Реализация алгоритма линейного поиска. Функция принимает список и элемент для поиска
# возвращает индекс элемента или -1, если элемент не найден

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# 02. Анализ временной и пространственной сложности
# Временная сложность:
# Наихудший случай: O(n), так как алгоритм проверяет все элементы списка.
# Лучший случай: O(1), если элемент находится в начале списка.
# Средний случай: O(n), так как в среднем алгоритм проверяет половину элементов списка.
# Пространственная сложность:
# O(1), так как алгоритм не использует дополнительную память.

# 03. Создайте список из 100 случайных чисел и выполните линейный
# поиск для нескольких различных значений.

random_list = [random.randint(1, 1000) for _ in range(100)]
test_values = [random_list[0], random_list[50], random_list[-1], 12345]
print("Список из 100 случайных чисел:", random_list)
for value in test_values:
    result = linear_search(random_list, value)
    if result != -1:
        print(f"Значение {value} найдено на позиции {result}.")
    else:
        print(f"Значение {value} не найдено в списке.")

# 04. Сравните время выполнения линейного поиска для разных
# размеров списков (например, 10, 100, 1000 элементов). Постройте
# график зависимости времени выполнения от размера списка
def time_for_linear_search():
    times = []
    sizes = [10, 100, 1000]
    s1 = '''def liner_search_test():
        arr = random.randint(1, 10)
        target = 9'''
    i = timeit.timeit(stmt=s1, number=200000)
    times.append(i)
    print('Время выполнения для списка 10 элементов', i)
    s2 = '''def liner_search_test():
        arr = random.randint(1, 100)
        target = 98'''
    j = timeit.timeit(stmt=s2, number=200000)
    times.append(j)
    print('Время выполнения для списка 100 элементов', j)
    s3 = '''def liner_search_test():
        arr = random.randint(1, 1000)
        target = 999'''
    n = timeit.timeit(stmt=s3, number=200000)
    times.append(n)
    print('Время выполнения для списка 1000 элементов', n)

    plt.plot(sizes, times, marker='o', label="Линейный поиск")
    plt.title("Зависимость времени поиска от размера списка")
    plt.xlabel("Размер списка")
    plt.ylabel("Время выполнения (секунды)")
    plt.grid()
    plt.legend()
    plt.show()

time_for_linear_search()