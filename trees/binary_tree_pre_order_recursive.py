from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.result

        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.result


s = Solution()

three = TreeNode(3)
two = TreeNode(2, three, None)
one = TreeNode(1, None, two)

result = s.preorderTraversal(one)
print(result)