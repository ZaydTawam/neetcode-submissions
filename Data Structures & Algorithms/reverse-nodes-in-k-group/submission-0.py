# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = before = ListNode(0, head)
        slow = fast = head
        i = 1
        while fast:
            if i % k != 0:
                fast = fast.next
                i += 1
                continue
            remaining_list = fast.next 
            prev = None
            curr = slow
            while curr != remaining_list and curr:
                curr.next, prev, curr = prev, curr, curr.next
            before.next = prev
            before = slow
            slow.next = curr
            slow = fast = curr
            i = 1
        
        return dummy_head.next
