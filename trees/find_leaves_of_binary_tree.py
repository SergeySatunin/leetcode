#https://leetcode.com/problems/find-leaves-of-binary-tree/solution/
from collections import deque
import itertools

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        super_leafs = []
        flattened_super_leafs = []
        while len(super_leafs) == 0 or super_leafs[-1] != [root]:
            leafs = []

            nodes = deque()
            nodes.append(root)

            while len(nodes) > 0:
                node = nodes.popleft()
                sl = flattened_super_leafs

                if ((not node.right or node.right in sl) and (not node.left or node.left in sl)):
                    leafs.append(node)
                if node.right and node.right not in sl:
                    nodes.appendleft(node.right)
                if node.left and node.left not in sl:
                    nodes.appendleft(node.left)

            super_leafs.append(leafs)
            flattened_super_leafs.extend(leafs)

        return [[y.val for y in x] for x in super_leafs]