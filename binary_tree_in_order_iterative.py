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
        self.stack = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.result

        current = root

        while len(self.stack) > 0 or current is not None:
            while current is not None:
                self.stack.append(current)
                current = current.left

            current = self.stack.pop()
            self.result.append(current.val)
            current = current.right

        return self.result


s = Solution()

three = TreeNode(3)
two = TreeNode(2, three, None)
one = TreeNode(1, None, two)

result = s.inorderTraversal(one)
print(result)