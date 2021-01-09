# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, pre: List[int], inord: List[int]) -> TreeNode:

        if not pre:
            return None

        if len(pre) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        root_ind = inord.index(root.val)

        left = inord[:root_ind]
        right = inord[root_ind + 1:]

        root.left = self.buildTree(pre[1:len(left) + 1], left) if left else None
        root.right = self.buildTree(pre[len(left) + 1:], right) if right else None

        return root

s = Solution()
result = s.buildTree([3,9,20,15,7], [9,3,15,20,7])

print()
