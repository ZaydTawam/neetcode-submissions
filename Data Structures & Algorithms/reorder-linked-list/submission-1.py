# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        ptr1, ptr2 = head, prev
        while ptr1 != ptr2 and ptr2.next:
            ptr1_next, ptr2_next = ptr1.next, ptr2.next
            ptr2.next, ptr1.next = ptr1.next, ptr2
            ptr1, ptr2 = ptr1_next, ptr2_next


