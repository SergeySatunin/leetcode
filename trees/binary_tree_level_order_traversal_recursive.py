from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = []

    def levelOrder(self, node):
        if not node:
            return None

        next_level =  [node]
        while next_level:
            next_level = self.get_level(next_level)

        return self.result

    def get_level(self, nodes):

        if not nodes:
            return None

        current_level = []
        next_level = []

        for n in nodes:
            current_level.append(n.val)

            if n.left is not None:
                next_level.append(n.left)

            if n.right is not None:
                next_level.append(n.right)

        self.result.append(current_level)
        return next_level


s = Solution()

five = TreeNode(5, None, None)
four = TreeNode(4, None, None)
three = TreeNode(3, None, None)
two = TreeNode(2, four, five)
one = TreeNode(1, two, three)

result = s.levelOrder(one)
print(result)