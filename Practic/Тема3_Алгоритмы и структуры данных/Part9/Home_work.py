class DirectedGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)

    def __repr__(self):
        return '\n'.join(f"{k}: {sorted(list(v))}" for k, v in self.adj.items())
print('___________________________________________________________')
print()
print("=== Реализация класса DirectedGraph ===")
print()
g = DirectedGraph()
g.add_vertex(1)
g.add_vertex(2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)
print(g)
print('___________________________________________________________')
print()

def bfs(graph, start):
    from collections import deque
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            order.append(v)
            queue.extend(graph.adj.get(v, []))
    return order

print("=== Осуществление поиска в ширину(BFS) ===")
print()
print(bfs(g, 1))
print('___________________________________________________________')
print()


def create_adjacency_matrix(edges):
    vertices = sorted(set(u for edge in edges for u in edge))
    idx_map = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    matrix = [[0]*n for _ in range(n)]
    for u, v in edges:
        matrix[idx_map[u]][idx_map[v]] = 1
    return matrix, vertices

def add_vertex_matrix(matrix, vertices, v):
    if v in vertices:
        return matrix, vertices
    vertices.append(v)
    for row in matrix:
        row.append(0)
    matrix.append([0]*len(vertices))
    return matrix, vertices

def add_edge_matrix(matrix, vertices, u, v):
    if u not in vertices or v not in vertices:
        raise ValueError("Вершины должны существовать")
    i, j = vertices.index(u), vertices.index(v)
    matrix[i][j] = 1

print("=== Матрица смежности ===")
print()
edges = [(1,2), (2,3), (1,3)]
matrix, vertices = create_adjacency_matrix(edges)
for row in matrix:
    print(row)
print("Вершины:", vertices)
print('___________________________________________________________')
print()

matrix, vertices = add_vertex_matrix(matrix, vertices, 4)
add_edge_matrix(matrix, vertices, 3, 4)
for row in matrix:
    print(row)
print("Вершины:", vertices)
print('___________________________________________________________')
print()

def create_adjacency_list(edges):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = set()
        adj[u].add(v)
        if v not in adj:
            adj[v] = set()
    return adj

def add_vertex_list(adj, v):
    if v not in adj:
        adj[v] = set()

def add_edge_list(adj, u, v):
    if u not in adj:
        adj[u] = set()
    if v not in adj:
        adj[v] = set()
    adj[u].add(v)

print("=== Список смежности ===")
print()
adj = create_adjacency_list(edges)
for k in sorted(adj):
    print(f"{k}: {sorted(list(adj[k]))}")
print('___________________________________________________________')
print()

add_vertex_list(adj, 4)
add_edge_list(adj, 3, 4)
for k in sorted(adj):
    print(f"{k}: {sorted(list(adj[k]))}")
print('___________________________________________________________')
print()