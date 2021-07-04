class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_unique_len = 0

    def preorderTraversal(self, root: TreeNode, visited: set, path_len):
        if visited is None:
            visited = set()

        if root is None or root.val in visited:
            self.max_unique_len = max(self.max_unique_len, path_len)
            return

        visited.add(root.val)
        path_len += 1
        self.preorderTraversal(root.left, visited, path_len)
        self.preorderTraversal(root.right, visited, path_len)
        visited.remove(root.val)


s = Solution()


I = TreeNode(5)
J = TreeNode(6)
H = TreeNode(2)
D = TreeNode(3,H)
E = TreeNode(6)
B = TreeNode(2, D, E)
F = TreeNode(3)
G = TreeNode(1, I, J)
C = TreeNode(3, F, G)
A = TreeNode(1, B, C)

s.preorderTraversal(A, None, 0)
print(s.max_unique_len)