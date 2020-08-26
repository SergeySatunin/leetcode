from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return root

        result = []
        queue = deque()

        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(current_level)

        return result


s = Solution()

three = TreeNode(3, None, None)
two = TreeNode(2, None, None)
one = TreeNode(1, two, three)

result = s.levelOrder(one)
print(result)