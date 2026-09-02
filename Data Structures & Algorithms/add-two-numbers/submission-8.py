# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        
        overflow = 0
        while l1 or l2:
            val = overflow
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            curr.next = ListNode(val % 10)
            overflow = val//10
            curr = curr.next
        
        if overflow:
            curr.next = ListNode(overflow)
        
        return dummy.next