# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        ptr = slow
        while ptr:
            ptr_next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = ptr_next
        
        l, r = head, prev
        while l != r and l.next != r:
            l_next, r_next = l.next, r.next

            l.next = r
            r.next = l_next

            l = l_next
            r = r_next
