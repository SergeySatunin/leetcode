# https://leetcode.com/problems/balanced-binary-tree/submissions/
from functools import lru_cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, node: TreeNode) -> bool:
        if not node or (not node.left and not node.right):
            return True
        else:
            left_height = self.height(node.left)
            righ_height = self.height(node.right)
            result = abs(left_height - righ_height) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right)

        return result

    @lru_cache
    def height(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))



fiveteen = TreeNode(15)
seven = TreeNode(7)
twenty = TreeNode(20, fiveteen, seven)
nine = TreeNode(9)
three = TreeNode(3, nine, twenty)

s = Solution()
result = s.isBalanced(three)

print(result)