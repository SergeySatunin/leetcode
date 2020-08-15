# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        s = f = head
        f_counter = s_counter = 1

        while f:
            f = f.next
            f_counter += 1

            while f_counter - s_counter > n + 1:
                s = s.next
                s_counter += 1

        if s == f and n == 1:
            return None

        if f_counter - s_counter == n:
            return s.next

        tmp = s.next.next
        s.next = tmp

        return head


l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)


s = Solution()
result = s.removeNthFromEnd(l1, 4)

while result:
    print(result.val)
    result = result.next
