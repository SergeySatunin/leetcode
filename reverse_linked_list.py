# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, p):
        tail = None

        while p:
            # store the next element in a temp variable so that we don't break the connection
            p_next = p.next
            # breaking the connection and pointing to the tail
            p.next = tail
            # setting the new "head" for the tail
            tail = p
            # moving on
            p = p_next

        return tail


l3 = ListNode(3)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

s = Solution()
result = s.reverseList(l1)

p = result
while p is not None:
    print(p.val)
    p = p.next

print()