# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr_res = ListNode()
        curr_l1 = l1
        curr_l2 = l2
        carry = 0
        while curr_l1 or curr_l2 or carry:
            num = (curr_l1.val if curr_l1 else 0) + (curr_l2.val if curr_l2 else 0) + carry
            first_digit = num % 10
            carry = num // 10
            print(first_digit, carry)
            curr_res.next = ListNode(first_digit)
            
            curr_res = curr_res.next
            curr_l1 = curr_l1.next if curr_l1 else None
            curr_l2 = curr_l2.next if curr_l2 else None
        
        
        return dummy.next

# 1

# 1->5->9
#         ^
# 4->5
#      ^

# d->5->0->0->1
#             ^