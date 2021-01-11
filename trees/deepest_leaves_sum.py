# https://leetcode.com/problems/deepest-leaves-sum/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val

        q = deque()
        q.append(root)

        level_leaf_sum = 0

        while q:
            level = []
            level_leaf_sum = 0

            for el in q:
                if el.left:
                    level.append(el.left)

                if el.right:
                    level.append(el.right)

                if el.left is None and el.right is None:
                    level_leaf_sum += el.val

            q = level

        return level_leaf_sum