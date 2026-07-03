# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head
        while True:
            min_node = None
            min_node_index = 0
            for i, node in enumerate(lists):
                if not node:
                    continue
                if not min_node or min_node.val > node.val:
                    min_node = node
                    min_node_index = i

            if not min_node:
                break
            
            lists[min_node_index] = min_node.next

            curr.next = min_node
            curr = curr.next
        
        return dummy_head.next