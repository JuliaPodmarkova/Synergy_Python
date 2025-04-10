from random import randint

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Попытка извлечь элемент из пустого стека")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Проверка верхнего элемента пустого стека")

if __name__ == "__main__":
    n = randint(1, 100)
    print(f"Факториал числа {n} = {factorial(n)}")
    print()

    my_list = []
    for i in range(10):
        my_list.append(randint(1, 100))
    print(f"Сумма элементов в списке {my_list} = {sum_of_list(my_list)}")
    print()

    sorted_list = []
    for i in range(10):
        sorted_list.append(randint(1, 100))
        sorted_list.sort()
    print(f'Список для поиска {sorted_list}')
    target = n
    index = binary_search(sorted_list, target, 0, len(sorted_list) - 1)
    if index != -1:
        print(f"Элемент {target} найден на индексе {index}")
    else:
        print(f"Элемент {target} не найден в списке")

    print()
    print('Работа со стеком')
    print('-----------------------')
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Верхний элемент стека для удаления: {stack.peek()}")
    print(f"Извлеченный элемент для просмотра: {stack.pop()}")
    print(f"Стек пуст? {stack.is_empty()}")