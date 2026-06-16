# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        dummy = ListNode()
        curr = dummy

        while ptr1 or ptr2:
            if not ptr1:
                curr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            elif not ptr2:
                curr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            elif ptr1.val <= ptr2.val:
                curr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                curr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            
            curr = curr.next
        
        return dummy.next



        




# 1->2->4
#         ^
# 1->3->5
#       ^

# 1->1->2->3->4->5
