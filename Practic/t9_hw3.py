# Задача 3. Поддиагональная сумма

def get_indices_for_diagonal_k(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    indices = []

    for i in range(k, rows):
        j = i - k
        if j < cols:
            indices.append((i, j))
    return indices

def sum_below_main_diagonal(matrix):
    indices = get_indices_for_diagonal_k(matrix, 1)
    total = 0
    for i, j in indices:
        total += matrix[i][j]
    return total

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2], [7, 8]]
c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(sum_below_main_diagonal(a))
print(sum_below_main_diagonal(b))
print(sum_below_main_diagonal(c))
print(sum_below_main_diagonal(d))
