# https://leetcode.com/problems/binary-tree-paths/

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.results = set()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.preorderTraversal(root, None)
        return list(self.results)

    def preorderTraversal(self, root: TreeNode, visited: List):
        if visited is None:
            visited = []

        if root is None:
            return

        visited.append(root.val)
        if root.left is None and root.right is None:
            self.results.add('->'.join([str(x) for x in visited]))

        self.preorderTraversal(root.left, visited)
        self.preorderTraversal(root.right, visited)
        visited.pop()


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

print(s.binaryTreePaths(A))
