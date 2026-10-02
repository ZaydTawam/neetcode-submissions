# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = head
        last_node = dummy
        list_length = 0
        while curr:
            list_length += 1
            last_node = last_node.next
            curr = curr.next
        
        rotations = list_length//k
        ptr1, ptr2 = dummy, last_node
        for i in range(rotations*k):
            if i % k == 0:
                while ptr2.next:
                    ptr2 = ptr2.next
            if ptr1.next is ptr2:
                continue
            ptr2.next, ptr1.next.next, ptr1.next = ptr1.next, ptr2.next, ptr1.next.next
        
        for i in range(list_length % k):
            while ptr2.next:
                ptr2 = ptr2.next
            if ptr1.next is ptr2:
                continue
            ptr2.next, ptr1.next.next, ptr1.next = ptr1.next, ptr2.next, ptr1.next.next
        
        return ptr1.next
        


# 6
# d->3->2->1->6->5->4->8->7
# ^                       ^

# ptr2.next, ptr1.next.next, ptr1.next = ptr1.next, ptr2.next, ptr1.next.next