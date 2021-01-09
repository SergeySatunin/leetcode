#https://leetcode.com/problems/sum-of-left-leaves/

class Solution:

    def __init__(self):
        self.sum = 0
        pass

    def helper(self, node: TreeNode, is_left):
        if node is None:
            return

        if node.left is None and node.right is None and is_left == True:
            self.sum += node.val

        if node.left is not None:
            self.helper(node.left, True)

        if node.right is not None:
            self.helper(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.helper(root, False)
        return self.sum