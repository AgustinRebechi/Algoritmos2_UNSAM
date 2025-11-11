from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# Ejemplo de uso:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)

# Crear un árbol de ejemplo
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(maxDepth(root))  # Salida: 3

def bfs(root):
    if root is None:
        return
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result

# Ejemplo de uso de BFS:
print(bfs(root))  # Salida: [[1], [2, 3], [4, 5]]

def bfs_2(root):
    queue = []
    queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Ejemplo de uso de BFS 2:
bfs_2(root)  # Salida: 1 2 3 4

def dfs_preorder_binary(tree):
    if not tree:
        return
    
    print(tree)
    dfs_preorder_binary(tree.left)
    dfs_preorder_binary(tree.right)

dfs_preorder_binary(root)  # Salida: 1 2 4 5 3

# Busca si un valor existe usando DFS: , Tiempo O(n), Espacio: O(n)
def dfs_valuesearch_binary(node, target):
    if not node:
        return False

    if node.value == target:
        return True
    
    return dfs_valuesearch_binary(node.left, target) or dfs_valuesearch_binary(node.right, target)

# Ejemplo de uso de DFS búsqueda de valor:
print(dfs_valuesearch_binary(root, 5))  # Salida: True

