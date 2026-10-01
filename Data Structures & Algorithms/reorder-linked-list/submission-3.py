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

        prev, curr = None, slow
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        
        ptr1, ptr2 = head, prev
        while ptr1 != ptr2 and ptr1.next != ptr2:
            ptr1.next, ptr2.next, ptr1, ptr2 = ptr2, ptr1.next, ptr1.next, ptr2.next        


# 1->2->3<-4
# ^        ^    

        

# 0->6->1->5->2
#             ^
#                   ^
