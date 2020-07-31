# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast.next is None or fast.next.next is None:
                return False

            fast = fast.next.next
            slow = slow.next

        return True

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l2

s = Solution()
result = s.hasCycle(l1)

print(result)
