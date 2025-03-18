# Задача 4. Матричное умножение

def multiply_matrices(matrix1, matrix2):

    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0]) if rows_matrix1 > 0 else 0
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0]) if rows_matrix2 > 0 else 0

    if cols_matrix1 != rows_matrix2:
        return []

    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

matrix1 =  [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
print(multiply_matrices(matrix1, matrix2))
print()
# Обращаю Ваше внимание, что в задаче у второго комплекта данных те же значения, что и у первого,
# соответственно результаты первого и второго комплекта данных будут идентичны
matrix1 =  [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
print(multiply_matrices(matrix1, matrix2))
print()
matrix1 = [[1, 2], [3, 4], [5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
print(multiply_matrices(matrix1, matrix2))
