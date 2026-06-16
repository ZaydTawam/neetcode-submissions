# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow and fast:
            if not fast.next or not fast.next.next:
                break
            fast = fast.next.next

            slow = slow.next

            if fast == slow:
                return True
        
        return False
        



# 1->2->3->4->2
#          ^
#          ^   