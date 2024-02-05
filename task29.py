import random
import time
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

# Приклад використання
arr = [12, 11, 13, 5, 6, 7]
print("Початковий масив:", arr)
sorted_arr = merge_sort(arr[:])
print("Відсортований масив:", sorted_arr)

# Генеруємо великий масив даних
data = [random.randint(1, 1000) for _ in range(10000)]

# Сортуємо та вимірюємо час для алгоритму злиття
start_time = time.time()
sorted_data = merge_sort(data[:])  # Копіюємо дані, щоб не впливати на оригінальний масив
end_time = time.time()

# Виводимо час сортування
print(f"Час сортування за допомогою Merge Sort: {end_time - start_time} секунд")



#task1

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.transposed_graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.transposed_graph[v].append(u)

    def dfs(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(node)

    def fill_order(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.transposed_graph[node]:
            if not visited[neighbor]:
                self.fill_order(neighbor, visited, stack)
        stack.append(node)

    def get_sccs(self):
        stack = []
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Transpose the graph
        self.transposed_graph = defaultdict(list)
        for i in range(self.vertices):
            for neighbor in self.graph[i]:
                self.transposed_graph[neighbor].append(i)

        # Reset visited array
        visited = [False] * self.vertices

        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc = []
                self.fill_order(node, visited, scc)
                sccs.append(scc)

        return sccs

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

sccs = g.get_sccs()
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)

#task2

INF = float('inf')


def floyd_warshall(graph):
    vertices = len(graph)

    # Initialize the distance matrix with the given graph
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(vertices)] for i in
            range(vertices)]

    # Update the distance matrix using all vertices as intermediaries
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example usage:
graph = [
    [0, 3, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

result = floyd_warshall(graph)

# Print the shortest paths
for i in range(len(result)):
    for j in range(len(result[0])):
        if result[i][j] == INF:
            print("INF", end=" ")
        else:
            print(result[i][j], end=" ")
    print()
