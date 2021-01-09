# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        if len(postorder) == 1:
            return TreeNode(postorder[0])

        root = TreeNode(postorder[-1])
        root_ind = inorder.index(root.val)

        left = inorder[:root_ind]
        right = inorder[root_ind + 1:]

        root.left = self.buildTree(left, postorder[:len(left)]) if left else None
        root.right = self.buildTree(right, postorder[len(left):len(left) + len(right)]) if right else None

        return root

s = Solution()
result = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

