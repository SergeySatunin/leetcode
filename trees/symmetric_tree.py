# https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isEqual(root, root)

    def isEqual(self, node_l: TreeNode, node_r: TreeNode) -> bool:

        if node_l is None and node_r is None:
            return True

        if node_l is None or node_r is None:
            return False

        return node_l.val == node_r.val and self.isEqual(node_l.left, node_r.right) and self.isEqual(
            node_l.right, node_r.left)


s = Solution()

three_l = TreeNode(3, None, None)
three_r = TreeNode(3, None, None)
four_l = TreeNode(4, None, None)
four_r = TreeNode(4, None, None)
two_l = TreeNode(2, None, three_r)
two_r = TreeNode(2, None, three_r)
one = TreeNode(1, two_l, two_r)


result = s.isSymmetric(one)
print(result)