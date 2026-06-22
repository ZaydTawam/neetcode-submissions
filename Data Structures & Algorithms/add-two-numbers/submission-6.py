# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import log10


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0

        i = 1
        curr1 = l1
        curr2 = l2
        while curr1 or curr2:
            if curr1:
                num1 += i*curr1.val
                curr1 = curr1.next
            if curr2:
                num2 += i*curr2.val
                curr2 = curr2.next
            i *= 10
        
        final = num1 + num2
        if final == 0:
            return ListNode(0)

        dummy = prev = ListNode()
        while final:
            prev.next = ListNode(final % 10)
            prev = prev.next
            final //= 10
        
        return dummy.next

        
