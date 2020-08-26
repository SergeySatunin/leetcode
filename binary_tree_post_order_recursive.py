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

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.result

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)

        return self.result


s = Solution()

three = TreeNode(3)
two = TreeNode(2, three, None)
one = TreeNode(1, None, two)

result = s.postorderTraversal(one)
print(result)