# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, node: TreeNode) -> TreeNode:
        if node is None:
            return

        leftTree = self.invertTree(node.left)
        rightTree = self.invertTree(node.right)

        node.left = rightTree
        node.right = leftTree

        return node



one = TreeNode(1, None, None)
three = TreeNode(3, None, None)

two = TreeNode(2, one, three)

six = TreeNode(6, None, None)
nine = TreeNode(9, None, None)

seven = TreeNode(7, six, nine)

four = TreeNode(4, two, seven)


s = Solution()
result = s.invertTree(four)

print()
