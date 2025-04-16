def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[n][m]

def count_partitions(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i, n+1):
            dp[j] += dp[j-i]
    return dp[n]

def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    print("___________________________________________________________________________")
    print('=== Задача о рюкзаке ===')
    print()
    weights = [2, 1, 3, 2]
    values = [12, 10, 20, 15]
    capacity = 5
    print("Максимальная стоимость рюкзака:", knapsack(weights, values, capacity))
    print("___________________________________________________________________________")

    print()
    print('=== Функция, которая находит длину наибольшей общей подпоследовательности (LCS) двух строк ===')
    print()
    s1, s2 = "AGGTAB", "GXTXAYB"
    print("Длина LCS:", lcs(s1, s2))
    print("___________________________________________________________________________")
    print()
    print("=== Пример для разбиений числа ==")
    print()
    n = 5
    print("Количество разбиений числа:", count_partitions(n))
    print("___________________________________________________________________________")
    print()
    print("=== Пример для алгоритма Флойда-Уоршелла ===")
    print()
    INF = float('inf')
    matrix = [
        [0, 3, INF, 5],
        [2, 0, INF, 4],
        [INF, 1, 0, INF],
        [INF, INF, 2, 0]
    ]
    shortest_paths = floyd_warshall(matrix)
    print("Матрица кратчайших расстояний:")
    for row in shortest_paths:
        print(row)