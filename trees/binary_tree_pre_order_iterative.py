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

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.result

        self.stack.append(root)

        while len(self.stack) > 0:
            top_el = self.stack.pop()
            self.result.append(top_el.val)

            if top_el.right is not None:
                self.stack.append(top_el.right)

            if top_el.left is not None:
                self.stack.append(top_el.left)

        return self.result


s = Solution()

three = TreeNode(3)
two = TreeNode(2, three, None)
one = TreeNode(1, None, two)

result = s.preorderTraversal(one)
print(result)