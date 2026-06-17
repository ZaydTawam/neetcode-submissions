# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        # 1->2->3->4
        #    ^   ^   
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        # 3->4
        # ^
        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        ptr1 = head
        ptr2 = prev
        # 1->4->2->3
        #       ^  ^
        while ptr1 != ptr2 and ptr2.next:
            ptr1_next, ptr2_next = ptr1.next, ptr2.next
            ptr2.next, ptr1.next = ptr1.next, ptr2
            ptr1, ptr2 = ptr1_next, ptr2_next
        

# 3->4->5->6
#    ^ 

# 0->1->2->3<-4<-5<-6
# ^                 ^

# 0->6->1->2->3<-4<-5
#       ^           ^

# 0->6->1->5->2->3<-4
#             ^     ^

# 0->6->1->5->2->4->3
#             ^     ^

# 1->2->3<-4<-5<-6
# ^              ^

# 1->6->2->3<-4<-5
#       ^        ^

# 1->6->2->5->3<-4
#             ^  ^

# 1->6->2->5->3->4
#             ^

# ptr1_next, ptr2_next = ptr1.next, ptr2.next
# ptr2.next, ptr1.next = ptr1.next, ptr2
# ptr1, ptr2 = ptr1_next, ptr2_next



