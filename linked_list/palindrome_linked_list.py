# https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

        result = True

        if head is None:
            return True

        slow = fast = head

        tail = None
        counter = 0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            if fast is None:
                counter += 1
            else:
                counter += 2

            slow_next, slow.next = slow.next, tail
            tail = slow
            slow = slow_next

        if counter % 2 == 0:
            slow = slow.next

        while tail:
            if tail.val != slow.val:
                result = False
                break
            else:
                tail = tail.next
                slow = slow.next

        return result


l4 = ListNode(1)
l3 = ListNode(1)
l2 = ListNode(0, l3)
l1 = ListNode(1, l2)

s = Solution()
result = s.isPalindrome(l1)

print(result)