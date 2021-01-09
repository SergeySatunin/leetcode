#https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

s = Solution()

nine = TreeNode(9, None, None)
fifteen = TreeNode(15, None, None)
seven = TreeNode(7, None, None)
twenty = TreeNode(20, fifteen, seven)
three = TreeNode(3, nine, twenty)

result = s.maxDepth(three)
print(result)
