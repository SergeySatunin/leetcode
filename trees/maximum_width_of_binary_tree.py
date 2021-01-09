# https://leetcode.com/problems/maximum-width-of-binary-tree/
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = deque()
        m = 0

        if root is None:
            return 0

        stack.append([root, 1])

        while stack:
            m = max(m, stack[-1][1] - stack[0][1] + 1)
            next_level = deque()

            while stack:
                cur, ind = stack.popleft()
                if cur.left:
                    next_level.append([cur.left, 2 * ind - 1])
                if cur.right:
                    next_level.append([cur.right, 2 * ind])

            stack = next_level

        return m


five = TreeNode(5, None, None)
four = TreeNode(4, None, None)
nine = TreeNode(9, None, None)
three = TreeNode(3, five, four)
two = TreeNode(2, None, nine)
one = TreeNode(1, three, two)

s = Solution()
print(s.widthOfBinaryTree(one))