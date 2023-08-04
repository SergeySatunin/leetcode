class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        index = 0

        odd_head = None
        previous_odd = None
        odd_tail = None

        even_head = None
        previous_even = None
        even_tail = None

        while head:
            if index % 2 == 0:
                if odd_head is None:
                    odd_head = head
                    previous_odd = odd_head
                else:
                    previous_odd.next = head
                    previous_odd = head
                odd_tail = head
            else:
                if even_head is None:
                    even_head = head
                    previous_even = even_head
                else:
                    previous_even.next = head
                    previous_even = head
                even_tail = head

            if head.next:
                head = head.next
            else:
                head.next = None
                break

            index += 1

        if even_tail:
            even_tail.next = None

        odd_tail.next = even_head

        return odd_head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
seven = ListNode(7)
eight = ListNode(8)


s = Solution()
s.oddEvenList(one)

print()
