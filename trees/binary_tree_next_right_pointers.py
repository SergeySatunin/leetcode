# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

class InorderTraversalSolution:
    def connect(self, root):

        if not root:
            return

        q = deque()
        q.append(root)

        while q:
            len_q = len(q)
            level = []

            for i in range(len_q):
                q[i].next = q[i+1] if i+1 < len_q else None

                if q[i].left:
                    level.append(q[i].left)
                if q[i].right:
                    level.append(q[i].right)

            q = level

        return root

class RecursiveSolution:
    def helper(self, left, right):
        if not left or not right:
            return

        if left is right:
            left.next = None
        else:
            left.next = right
            self.helper(left.right, right.left)

        self.helper(left.left, left.right)
        self.helper(right.left, right.right)

    def connect(self, root):
        self.helper(root, root)
        return root



