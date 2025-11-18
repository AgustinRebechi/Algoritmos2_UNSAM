from collections import deque
# Grafo lista adyacencia
graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

# Recorrido grafo BFS FIFO

def bfs(graph, start):
    # Time: O(V+E)
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end="")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')
print('\n') 

# Recorrido grafo DFS recursivo y iterativo: LIFO

def dfs_recursivo(graph, node, visited=None):
    # Time: O(V+E)
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end='')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursivo(graph, neighbor, visited)

dfs_recursivo(graph, 'A')
print('\n')

def dfs_iterativo(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end='')
            visited.add(node)
            stack.extend(reversed(graph[node]))

dfs_iterativo(graph, 'A')
print('\n')

# Calcular la profundidad máxima de un árbol binario usando DFS y BFS

