# https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.traverse(root, sum, 0)

    def traverse(self, node, target_sum, current_sum):
        if node is None:
            return False

        if node.left is None and node.right is None:
            return (current_sum + node.val) == target_sum
        else:
            return self.traverse(node.left, target_sum, current_sum + node.val) \
                   or self.traverse(node.right, target_sum, current_sum + node.val)


nine = TreeNode(9, None, None)
fifteen = TreeNode(15, None, None)
seven = TreeNode(7, None, None)
twenty = TreeNode(20, fifteen, seven)
three = TreeNode(3, nine, twenty)

s = Solution()
result = s.hasPathSum(three, 30)

print(result)
