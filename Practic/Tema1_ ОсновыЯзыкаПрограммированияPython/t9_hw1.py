# Задача 1. Разглаживание вложенных списков

def flatten_list(list_1):
    flat_list = []
    for i in list_1:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([1, 2, [3, 4, [5, 6]], 7, [8]]))
print()
print(flatten_list([1, [2, [3, [4, [5, [6, [7, [8,
[9, [0]]]]]]]]]]))
print()
print(flatten_list([1, 2, 3.14, 4, 5, 6, 7 , 8, 9]))
