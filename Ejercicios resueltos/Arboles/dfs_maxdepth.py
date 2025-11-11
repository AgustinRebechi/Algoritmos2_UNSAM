from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    def dfs(node):
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        return max(left_depth, right_depth) + 1
    
    return dfs(root)

def maxDepth_bfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    nivel = 0
    fila = deque([root])

    while fila:
        for i in range(len(fila)):
            nodo = fila.popleft()
            if nodo.left:
                fila.append(nodo.left)
            if nodo.right:
                fila.append(nodo.right)
        nivel += 1
    return nivel

# Ejemplo de uso:

    
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
print(maxDepth_bfs(root))
print(maxDepth(root))
   