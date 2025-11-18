from collections import deque


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS
    def maxDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    # DFS recursivo
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    # DFS iterativo
    def maxDepth_I(self, root:TreeNode) -> int:
        if not root:
            return 0
        stack = [[root,1]]
        res = 1
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.left,depth + 1])
                stack.append([node.right, depth + 1])
        return res

# Ejemplo

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

def main():
    solution = Solution()
    print(solution.maxDepth_bfs(root))
    print(solution.maxDepth(root))
    print(solution.maxDepth_I)

if '__main__' == __name__:
    main()


